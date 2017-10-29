# Rental House Information Query System
Design a rental house information query system to provide user information about rental house information. Similar to Craigslist.

## Features
- Keeps track of rental information.
- Allows users to subscribe by emails for interested rental categories.
- Notifies subscribers if there is any match house info in the subscribed categories.
- Also allows users to query rental house information online.
- Filter queries based on user's demands.

## Development environment
- **MySQL DB** is used to store categories, product list urls, products and users information.
- **Mongo DB** is used to store product crawling logs.
- **Lombok** is used to eliminate constructors and getter/setter implementation for cleaner coding style.
- **RabbitMQ** Messages delivery and inspection tool.
- **BS4** is used to retrieve web page content, parse the required text from the page.
- **Spring Boot** is used for fast REST API implementation.
- **Maven** Dependences management.
- **Spring Boot Actuator** is used to provide monitoring information. (/health, /metrics... etc.)
- **Spring Cloud** is used to provide infrastructure services.
-- **Angular JS** is used to front end implements.

## Design Diagrams
### System Design
![Overview](/Overview.png)

### DataBase Desgin
![MySQL Schema](/MySQLSchema.png)

### Back-End Architecture
![arch](/arch.png)


## Getting Started
First of all, run Crawler.py file. It will get all rental information from websites based on raw query file. It will take
couple hours to finish crawling Los Angeles County rental info.  

Secondly, run SQL.py file to process data.

Finally, start back end service. Service will start on tomcat 9001.

## LICENSE

[MIT](./License.txt)
