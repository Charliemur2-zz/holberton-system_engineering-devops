<img src="">

# Repository Title Goes Here

SQL Replication
If your important data is stored in an SQL database (MySQL, MariaDB, PostgreSQL, etc.), you can take advantage of some built-in replication features. These can be used to provide a failover system in case the main server goes down.

Master-Slave Replication
The most basic kind of SQL replication is a Master-Slave configuration. In this scenario, you have a main database server, which is referred to as the “master” server. This server is responsible for performing all writes and updates. The data from this server is copied continuously to a “slave” server. This server can be be read from, but not written to.

This setup allows you to distribute the reads across multiple machines, which can dramatically improve your application’s performance.

While this performance increase is an advantage, one of the main reasons you may set up master-slave replication is for handling failover. If your master server becomes unavailable, you can still read from your slave server. Furthermore, it is possible to convert the slave into a master server in the event that your master is offline for an extended period of time.

Master-slave replication is, in fact, one area where we begin to see how redundancy and backups can complement each other. In a master-slave configuration, you can replicate data from the master to the slave. You can then temporarily disable replication to maintain a consistent state of information on the slave. From here, you can back up the database using whatever backup mechanism is appropriate.

To learn more about how to configure MySQL master-slave replication, click here. To learn about how to accomplish master-slave replication with PostgreSQL, follow this link.

Master-Master Replication
A second form of replication is called Master-Master replication. This configuration allows both servers to have “master” abilities. This means that each server can accept writes and updates and will transfer the changes to the opposite server. This configuration inherits the advantages of the master-slave setup, but also benefits from increased write performance if the writes are properly distributed by a load balancing mechanism.

This also means that, in the event that one server goes down, the other is still up and ready to accept requests. While the configuration is more complicated, the failover in the event of a problem is less complicated than the master-slave redundancy, because the slave database does not need to transform into the master.

This configuration can also be combined with a backup mechanism if you take one of the master servers offline. You must maintain a static database for backups to function correctly, so you have to ensure that no data is being modified or written to until after the backup is complete.


---

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [Support](#support)
- [License](#license)

---

## Installation

Copy the code, compile (if is necessary), and execute it.


## Features
## Usage

See the codes of different functions and programs.

## Documentation

<a href="https://intranet.hbtn.io/rltoken/yI-YnEyAx2mO5qqmbrCTbw">`What is a primary-replica cluster`</a><br>
<a href="https://intranet.hbtn.io/rltoken/M2mXERIEQA7w0Pkj85nTNw">`MySQL primary replica setup`</a><br>
<a href="https://intranet.hbtn.io/rltoken/7C7YTJOU2iR_kZDQLPhl1A">`Build a robust database backup strategy`</a><br>

---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using.
---

## Team

https://github.com/Charliemur2
---

## Support

Feel free to contact me!

- GitHub at <a href="https://github.com/Charliemur2">`Charliemur2`</a>
- Twitter at <a href="https://twitter.com/charliesoka">`@charliesoka`</a>
- Insert more social links here.

---

## License

Free Source Code
