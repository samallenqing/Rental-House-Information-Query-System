# Rental House Information Query System
Design a rental house information query system to provide user information about rental house information. Similar to Craigslist.

## Features
- Keeps track of rental information.
- Allows users to subscribe by emails for interested rental categories.
- Notifies subscribers if there is any match house info in the subscribed categories.
- Also allows users to query rental house information online.

## Development environment
- **MySQL DB** is used to store categories, product list urls, products and users information.
- **Mongo DB** is used to store product crawling logs.
- **Lombok** is used to eliminate constructors and getter/setter implementation for cleaner coding style.
- **RabbitMQ** Messages delivery and inspection tool.
- **Memcached** is used to provide expedite query response.
- **BS4** is used to retrieve web page content, parse the required text from the page.
- **Spring Boot** is used for fast REST API implementation.
- **Maven** Dependences management.
- **Spring Boot Actuator** is used to provide monitoring information. (/health, /metrics... etc.)
- **Spring Cloud** is used to provide infrastructure services.

## Design Diagrams
![Overview](/Overview.png)
![MySQL Schema](/MySQLSchema.png)
![Memcached Schema](/Memcached.png)

### Start MongoDB

## Getting Started

## LICENSE

[MIT](./License.txt)
