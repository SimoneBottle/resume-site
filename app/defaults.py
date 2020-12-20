"""
Summary
-------
The summary is a brief intro. You can put raw HTML into this field.
"""
summary = "<p>Data obsessed with a financial academic background, try to improveevery day my analytics skills. Curious about every application in Data Science world. At the moment i'm really busy as DevOps Engineering team member in a data-intensive (PaaS) distributed web app project. What basically i'm doing every day is to carefully monitor each App components with the help of a complex set of real time dashboard. I'm also responsable of the integrity and quality of the data layer exposed to the client (big player in the automotive market) for BI/Analytics purposes.</p>"


languages = [
        ['Italian', ' (Native)'],
        ['English', ' (Intermediate)'],
        ['Spanish', ' (Fluent)']
        ]

education = [
        ['Laurea Triennale Economia e Gestione Aziendale', 'Università Europea di Roma', '2007 - 2011'],
        ['Erasmus Project - Administración y Dirección de Empresas', 'Universidad Francisco de Vitoria', '2013 - 2013'],
        ['Laurea Magistrale Economia, Managament e Finanza', 'Università Europea di Roma', '2011 - 2014']
        ]

interests = ['Yoga', 'Plants', 'Food']

skills = [
        ['Python', '70%'],
        ['Python - Dash', '60%'],
        ['Jupyter Notebook', '70%'],
        ['Spark - PySpark', '40%'],
        ['SQL', '80%'],
        ['ElasticSearch', '80%'],
        ['Power BI', '85%'],
        ['PowerShell', '50%'],
        ['Azure Ecosystem', '50%']
        
        ]

"""
Experience
----------
This should be a list of lists. Each sublist corresponds to a particular job
and is of the form:
    ['Title', 'Date range', 'Company name and location', 'Description of role']

The 'Description of role' field does not get escaped by the templating engine,
so you can put raw HTML in it if you like.
"""
experience = [
        ['Data Engineer - DevOps Team Member',
            '2018 - Present',
            'PA Evolution, Rome',
            '<p>- Design/deploy/deliver big data pipelines;<br>- Monitor all componenets/processes related to the app constantly focused on improving performance and avoiding problems;<br>- Make time series analysis of cloud web servers metrics in orders to scale up/down the VMs to avoid useless costs;<br>- Create custom event for alerting based on thresholds calculated with anomaly detenction approach;<br>- Support the qa team and qa team in bug fixing;<br>- Support the client directly in tasks related to my field.<br>- Responsable of the integrity and quality of the data layer exposed to the client for BI/Analytics purposes.</p>'
        ],
        ['Marketing Data Anylist',
            '2017 - 2018',
            'GEKO S.p.A., Rome',
            '<p>- Create data mart with data scraped on competitors website;<br>- Generate dashboard/reports with customer churn rate/retention KPI;<br>- Product price analysis;<br>- Offer insights about new products potential;<br>- Examine a campaign&apos;s return on investment;<br>Technologies used: SQL, PowerBI, Python, R</p>'
        ],
        ['Reporting Specialist',
            '2014 - 2017',
            'GEKO S.p.A., Rome',
            '<p>- Design and execute automated procedures interfacing with systems to report business analytics and sales support indicators;<br>- Generate periodic reports with accuracy to identify and process data sources;<br>- Develop queries to extract data on department needs;<br>- Test reports and use problem solving skills to determine problems&rsquo; root cause and suggest solutions with users;<br>- Discuss with staff, users and management to develop requirements to create new report or revise current report.<br>Technologies used: SQL, SSRS, SSIS, SSAS.</p>'
        ]
    ]

"""
Projects
--------
The project_intro field is for a short introduction to your work.
Project are a list of lists, where each sublist refers to a specific project,
and is of the form:
    ['Title', 'Description', 'Link to project webpage']

project_intro = '<p>You can list your side projects or open source libraries in this section. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et ligula in nunc bibendum fringilla a eu lectus.</p>'
projects = [
        ['Velocity',
            'A responsive website template designed to help startups promote, market and sell their products.',
            '#hook'
        ],
        ['DevStudio',
            'A responsive website template designed to help startups promote, market and sell their products.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-web-development-agencies-devstudio/'
        ],
        ['Tempo',
            'A responsive website template designed to help startups promote their products or services and to attract users &amp; investors.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-for-startups-tempo/'
        ],
        ['Atom',
            'A comprehensive website template solution for startups/developers to market their mobile apps.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-mobile-apps-atom/'
        ],
        ['Delta',
            'A responsive Bootstrap one page theme designed to help app developers promote their mobile apps.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-for-mobile-apps-delta/'
        ]
    ]

"""



"""
default_data
------------
This dictionary puts everything together. It will be read by the Flask app when
it is instantiated.
"""
default_data = {
    'site_title' : 'Simone Napolitano Resume Web Site',
    'name' : 'Simone Napolitano',
    'tagline' : 'Data Engineer',
    'email' : 'napolitano.sim@gmail.com',
    'phone' : '+39 3246199079',
    'website' : 'Based in Rome',
    'linkedin' : 'linkedin.com/in/napolitanosimone',
    'languages' : languages,
    'education' : education,
    'interests' : interests,
    'skills' : skills,
    'summary' : summary,
    'experience' : experience
    #'project_intro' : project_intro,
    #'projects' : projects
    }
