from xml.etree.ElementTree import parse

tree = parse("students_info.xml")

root = tree.getroot()
child = root.getiterator()

for student in child :
    for stu in student :
        print("=" * 60)

        print("성별 :", stu.get("sex"))
        print("이름 :", stu.get("name"))

        print("전공 :", stu.findtext("major"))

        for language in stu.getiterator("practicable_computer_languages") :
            for lang in language :
                print("-" * 30)

                print("언어 이름 : ", lang.get("name"))
                print("언어 등급 : ", lang.get("level"))
                # print ("언어 기간 :", lang.get
    break


