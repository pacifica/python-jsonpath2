# Example Usage

The usage of the Policy API is strictly a read-only interface. The
command line usage of the system provides tools to update data in
the metadata API and are mostly cronjob like processes.

## The API

The policy server is split up into endpoints named for their Pacifica
project that utilizes them. So the path `/uploader` is used by the
Pacifica Uploader (http://github.com/pacifica/pacifica-uploader) to
control its behavior. The idea is that workflow implemented by the
various Pacifica projects has some element of site or instance
specific policy that can be applied to the running service. The policy
is driven by the metadata and thus this project should talk to the
metadata service.

### Events API

The Events API is used by the
[Notifications](https://github.com/pacifica/pacifica-notifications)
service. The role of this query is to verify the event recieved by
the Notifications services is allowed to be sent to the user on the
URL path.

Request Example:
```
POST /events/dmlb2001
Content-Type: application/json
{
  "data": [
    ...
  ]
}
```

Good Response Example:
```
Http-Code: 200
{
  "status": "success"
}
```

Failed Response Example:
```
Http-Code: 401
{
  "error": "..."
}
```

The underlying logic for this implementation is the same as the
ingest endpoint discussed next.

### Ingest API

The Ingest API is used by the
[Ingest](https://github.com/pacifica/pacifica-ingest) service. This
endpoint verifies the relationships between user, project and
instrument before allowing an upload. The content of the body
document is defined by the
[uploader](https://pacifica-uploader.readthedocs.io/en/latest/metadataconfig.html).

Request Example:
```
POST /ingest
Content-Type: application/json
[
  ...
]
```

Good Response Example:
```
Http-Code: 200
{
  "status": "success"
}
```

Failed Response Example:
```
Http-Code: 401
{
  "error": "..."
}
```

### Reporting and Status API

This document is not going into details about these APIs currently.
These endpoints are supposed to be used by tools that provide status
of current uploads to users of Pacifica as well as institutional
reporting tools that aggregate metrics about uploads in Pacifica.
Eventually, Pacifica should have a basic set of these websites to
allow users to use these endpoints but not currently.

### Uploader API

The Uploader API is a simple query interface to get complex metadata
interactively while users are using the Uploader. This API has a JSON
document that looks very SQL like but is not complete.

Request Example:
```
POST /uploader
Content-Type: application/json
{
  "user": 100,
  "from": "instruments",
  "columns": [
    "_id",
    "name"
  ],
  "where": {
    "_id": 54
  }
}
```

Good Response Example:
```
Http-Code: 200
[
  {
    "_id": 54,
    "name": "NMR PROBES: Nittany Liquid"
  }
]
```

Failed Response Example:
```
Http-Code: 500
```

## Admin Command Line

There is a single admin command line tool (`pacifica-policy-cmd`)
with two subcommands, `data_release` and `searchsync`. The
`data_release` subcommand handles setting the `data_release`
attributes of the Projects and Transactions. The `searchsync`
subcommand handles formatting and synchonizing metadata to
[ElasticSearch](https://www.elastic.co/products/elasticsearch).

```
$ pacifica-policy-cmd --help
usage: pacifica-policy-cmd [-h] [--verbose] {data_release,searchsync} ...

positional arguments:
  {data_release,searchsync}
                        sub-command help
    data_release        data_release help
    searchsync          searchsync help

optional arguments:
  -h, --help            show this help message and exit
  --verbose             enable verbose debug output
```

### Data Release

The data release process involves two phases, updating the suspense
date and setting data release. The suspense date is a date that the
metadata and data associated with that object in metadata will be
released in the future. The data release phase checks the suspense
date with now to determine if the object needs to have it released.

```
$ pacifica-policy-cmd data_release --help
usage: pacifica-policy-cmd data_release [-h]
                                        [--exclude [EXCLUDE [EXCLUDE ...]]]
                                        [--keyword KEYWORD]
                                        [--time-after TIME_AFTER]
                                        [--time-ago TIME_AGO]

data release by policy

optional arguments:
  -h, --help            show this help message and exit
  --exclude [EXCLUDE [EXCLUDE ...]]
                        id of keyword prefix to exclude.
  --keyword KEYWORD     keyword one of projects.actual_end_date,
                        projects.actual_start_date, projects.submitted_date,
                        projects.accepted_date, projects.closed_date,
                        transactions.created, transactions.updated.
  --time-after TIME_AFTER
                        set suspense date on data to X days after keyword.
  --time-ago TIME_AGO   only objects updated after X days ago.
```

### Search Sync

The search synchronization to Elasticsearch is driven by the Policy
service. The metadata in Elasticsearch is meant to be consumed by
client applications and in order to be performant those clients
should communicate directly with Elasticsearch. This does mean that
the metadata in Elasticsearch is not as current as the Metadata API.

```
$ pacifica-policy-cmd searchsync
usage: pacifica-policy-cmd searchsync [-h] [--objects-per-page ITEMS_PER_PAGE]
                                      [--threads THREADS]
                                      [--time-ago TIME_AGO]

sync sql data to elastic for search

optional arguments:
  -h, --help            show this help message and exit
  --objects-per-page ITEMS_PER_PAGE
                        objects per bulk upload.
  --threads THREADS     number of threads to sync data
  --time-ago TIME_AGO   only objects newer than X days ago.
```
