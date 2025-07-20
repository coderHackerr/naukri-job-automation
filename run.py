from naukri.main import Naukri

with Naukri() as bot:
    bot.land_frst_page()
    bot.login()
    bot.enter_mail()
    bot.enter_password()
    bot.loggin_btn()
    bot.search_btn()
    bot.enter_job()
    bot.enter_location()
    bot.expand_btn()
    bot.job_btn()
    bot.job_search_btn()
    bot.scrape_jobs()