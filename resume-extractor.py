import pdfplumber

pdf_list=[
        'Resume.pdf', 
        '2015 KiranKalsiResume (1).pdf', 
        'A_satish_Hyderabad_-_Secunderabad_5.08_yrs.pdf',
        'Ajay_Kumar_Hyderabad_-_Secunderabad_3.01_yrs.pdf',
        'Amit-Kumar-Mishra.pdf',
        'Android Java Spring CV Umair  Shaik.pdf',
        'Android Resume new progment 2.7yearss.pdf',
        'Anil Kumar Bathini Resume on 27July2015 - Project(Tech) Lead-4.pdf'

    ]
    
for item in pdf_list:
    all_text =''
    with pdfplumber.open(item) as pdf:
        for pdf_page in pdf.pages:
            single_page_text = pdf_page.extract_text()
            all_text = all_text + '\n' + single_page_text

    f = open(f'{item}.txt',"w+")
    f.write(all_text)
    f.close()
    print(f":::::::DONE--{item} :::::::::")