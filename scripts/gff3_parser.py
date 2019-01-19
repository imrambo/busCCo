#!/usr/bin/python3
#------------------------------------------------------------------------------
def gff3_parser(gff_file, program='general'):
    """
    Parse GFF3 files and return a dictionary.
    For program, specify 'prodigal' or 'minced'
    to parse GFF3 files specifically for these
    programs. Otherwise, the default 'general'
    won't do anything special.

    Option 'prodigal' is set for Prodigal version 2.x output.
    """
    import warnings
    import re

    gff_dict = {}
    with open(gff_file, 'r') as gff:
        for record in gff:
            if not record.startswith('#'):
                record = record.rstrip()
                recordList = record.split()
                seqid = recordList[0]
                source = recordList[1]
                ftype = recordList[2]
                start = recordList[3]
                end = recordList[4]
                score = recordList[5]
                strand = recordList[6]
                phase = recordList[7]
                attributes = recordList[8]
                attributes_list = attributes.split(';')
                if program == 'general':
                    gff_dict[seqid] = {'source':source, 'type':ftype,
                    'start':start, 'end':end, 'score':score, 'strand':strand,
                    'phase':phase, 'attributes':attributes_list}

                elif program == 'minced':
                    crispr_repeat = str()
                    if re.match(r'ID\=CRISPR\d+\;rpt_family\=CRISPR;rpt_unit_seq\=[A-Z]+', attributes) and ftype == 'repeat_region':
                        crispr_repeat = re.findall(r'rpt_unit_seq\=([A-Za-z]+)$', attributes_list[2])[0]
                        crispr_parent_id = attributes_list[0].split('=')[1]
                        gff_dict[crispr_parent_id] = {'seqid':seqid,'type':ftype,
                        'start':start,'end':end,'n_repeat':score,'repeat_sequence':crispr_repeat}

                    else:
                        crispr_parent_id = attributes_list[0].split('=')[1]
                        crispr_child_id = attributes_list[1].split('=')[1]
                        gff_dict[crispr_child_id] = {'seqid':seqid,'type':ftype,
                        'start':start,'end':end,'n_repeat':score,'repeat_sequence':gff_dict[crispr_parent_id]['repeat_sequence']}

                elif program == 'prodigal':
                    id = attributes_list[0].split('=')[1]
                    ordid = id.split('_')[1]
                    partial = attributes_list[1].split('=')[1]
                    start_type = attributes_list[2].split('=')[1]
                    #stop_type = attributes_list[3].split('=')[1]
                    rbs_motif = attributes_list[3].split('=')[1]
                    rbs_spacer = attributes_list[4].split('=')[1]
                    gc_cont = attributes_list[5].split('=')[1]
                    #gc_skew = attributes_list[7].split('=')[1]
                    confidence = attributes_list[6].split('=')[1]
                    cscore = attributes_list[7].split('=')[1]
                    sscore = attributes_list[8].split('=')[1]
                    rscore = attributes_list[9].split('=')[1]
                    uscore = attributes_list[10].split('=')[1]
                    tscore = attributes_list[11].split('=')[1]
                    #mscore = attributes_list[14].split('=')[1]

                    seqid = '%s_%s' % (seqid, ordid)
                    gff_dict[seqid] = {'source':source, 'type':ftype,
                    'start':start, 'end':end, 'score':score, 'strand':strand,
                    'phase':phase, 'partial':partial, 'start_type':start_type,
                    'rbs_motif':rbs_motif, 'rbs_spacer':rbs_spacer,
                    'gc_cont':gc_cont, 'confidence':confidence, 'cscore':cscore,
                    'sscore':sscore, 'rscore':rscore, 'uscore':uscore,
                    'tscore':tscore}

                else:
                    warnings.warn('no gff parsing method specified')

    return gff_dict
#==============================================================================
def pilercr_report2gff(target, source, env):
    """
    Parse the PilerCR report Summaries by Position and convert into GFF3 format.
    """
    with open(source, 'r') as pilercr, open(target, 'w') as pilercr_gff:
        lines = pilercr.readlines()
        linePos = [i for i,x in enumerate(lines) if x == 'SUMMARY BY POSITION\n'][0]
        posSummary = ''.join(lines[linePos+1:])
        posSummaryList = posSummary.split('>')
        posSummaryList = [ps.split('\n') for ps in posSummaryList]
        for ps in posSummaryList:
            match = [p.lstrip() for p in ps if re.match(r'\s+\d+.*?\s+[\d+\s+]{5}[GATC]+', p) or re.match(r'^\S+$', p)]
            if match:
                matchLists = [m.split() for m in match[1:]]
                gffRecords = ['\t'.join([match[0],'pilercr:1.06', 'repeat_region', m[2], str(int(m[2])+int(m[3])), m[4], '.', '.', 'ID=CRISPR%s;rpt_family=CRISPR;rpt_unit_seq=%s' % (m[0], m[-1])]) for m in matchLists]
                for g in gffRecords:
                    pilercr_gff.write(g + '\n')
            else:
                pass
    return None

#==============================================================================
def minced_gff2fasta(target, source, env):
    """
    Write a FASTA file of CRISPR repeat sequences parsed from a
    MinCED GFF3 output file.
    """
    import re
    from gff3_parser import gff3_parser
    minced_dict = gff3_parser(source, program = 'minced')
    repeats = [('>%s|%s' % (subdict['seqid'], key), subdict['repeat_sequence']) for key, subdict in source if re.match(r'CRISPR\d+$', key)]
    with open(target, 'w') as tout:
        for r in repeats:
            tout.write('%s\n%s\n' % (r[0], r[1]))
    return None
#==============================================================================
