# Ponisha Projects

This repository was created for first assignment of information Retrieval course in Shahid Beheshti University.
It is a simple python code that crawls freelance projects from [Ponisha](https://www.ponisha.ir) website using scrapy.
Data will be saved in MongoDB database.

## Install

```
$ git clone https://github.com/rferdosi/ponisha_projects.git
$ cd ponisha_projects
$ python3 setup.py install
```

## Extracted data

Eech project looks like this sample:

```
  {
    "short_link": "http://pnsh.co/p154883",
    "applicants_number": "0",
    "budget": "10,000,000",
    "creator": "kheshteaval",
    "description": "*یک سایت وردپرسی مورد نیاز است که در دسته بندی های گوناگون مشاغل مربوط مهاجرت مانند دفاتر جهانگردی و مهاجرتی , هتل ها , مهمان سراها , دفاتر هواپیمایی ,دارلترجمه ها ,رنت خودرو , تورها و تخفیفات و غیره امکان معرفی مشاغل خود را داشته باشند(با ثبت نام و امکان دسترسی به پنلشان) مشاغل دارای تفکیک استان و دسته بندی کامل باشند\n*یک دسته مقالات با چند زیر شاخه \n*امکان ویژه کردن کادر مشاغل و بروزرسانی با پرداخت هزینه\n*ایجاد افزونه پرداخت هزینه مشاوره و نوبت دهی مختص خود سایت و ادمین سایت فقط نه دیگران\n*و صفحه اول چند انجمن ایجاد میشود و یک تالار گفتگو جامع که بازدیدکنندگان امکان ایجاد تاپیک و پرسش و پاسخ دارند.",
    "skills": ["MySQL", "PHP", "CSS", "برنامه نویسی تحت وب"],
    "title": "سایت معرفی مشاغل و تالار گفتگوی وردپرسی",
    "remaining_time": "14 روز, 22 ساعت"
  }
```

## Spider

This project contains one spiders and you can see it using the list command:

```
$ scrapy list
ponisha
```

## Running the spider

You can run a spider using the scrapy crawl command, such as:

```
$ scrapy crawl ponisha
```

If you want to save the scraped data to a file, you can pass the -o option:

```
$ scrapy crawl ponisha -o projects.json
```

## Running the spider on schedule

You can schedule to run the ponisha spider every 10 hours with this command:

```
$ python main.py
```
