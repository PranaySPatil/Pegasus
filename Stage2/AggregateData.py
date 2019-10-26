import os
import CassandraHelper
import xml.etree.ElementTree as xml

def extract_info_from_source(source_path):
    unanswered_questions = 0
    total_questions = 0
    answered_questions = 0
    questions_with_answers_count = 0
    answers_count = 0
    all_tags = {}

    context = xml.iterparse(source_path, events=("start", "end"))
    context = iter(context)
    event, root = context.next()

    for event, elem in context:
        if event == "end":
            if elem is not None and elem.attrib.has_key('PostTypeId') and elem.attrib['PostTypeId'] == '1':
                total_questions += 1
                if not elem.attrib.has_key('AcceptedAnswerId'):
                    unanswered_questions += 1
                if elem.attrib.has_key('Tags'):
                    elem_tags = elem.attrib['Tags'][1:-1].split('><')
                    for tag in elem_tags:
                        if all_tags.has_key(tag):
                            all_tags[tag] += 1
                        else:
                            all_tags[tag] = 1
                if elem.attrib.has_key('AnswerCount'):
                    questions_with_answers_count += 1
                    answers_count += int(elem.attrib['AnswerCount'])
            root.clear()

    sorted_tags = sorted(all_tags.items() ,  key=lambda x: x[1] )
    sorted_tags.reverse()
    trending_tags = [i[0] for i in sorted_tags][0:10]
    trending_tags = ",".join(trending_tags)
    average_answers_count = int(answers_count/questions_with_answers_count)

    return total_questions, unanswered_questions, trending_tags, average_answers_count

posts_file_name_suffix = "\\Posts.xml"
data_source = os.path.abspath("Stage2//Stage2_data")
walk = os.walk(data_source)
data_source_directories = [x[0] for x in walk]
data_source_directories = data_source_directories[1:]

print("Starting processing for " + str(len(data_source_directories)) + " sources")
for data_source in data_source_directories:
    data_source_path = data_source + posts_file_name_suffix
    total_questions, unanswered_questions, trending_tags, average_answers_count = extract_info_from_source(data_source_path)
    domain_name = data_source.split("\\")[-1].split(".")[0]
    CassandraHelper.insert_values_in_posts_column_family(domain_name, total_questions, unanswered_questions, trending_tags, average_answers_count)
    print("Loaded " + domain_name)