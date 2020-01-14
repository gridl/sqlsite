# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New `redirect` handler to redirect incoming requests to other locations.

### Changed
- The SQLite database is now opened in read-only mode (`SQLITE_OPEN_READONLY`).
- BACKWARDS INCOMPATIBLE: changed to new `<type:param>` URL parameter syntax.
- BACKWARDS INCOMPATIBLE: changed the `exists_query` column to `existsquery`.


## [0.0.1] - 2019-01-12

Initial release.