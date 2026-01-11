# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project attempts to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## UNRELEASED - TBC

### Added

- `IntVector2.__str__`, `__repr__` to match `pygame.math.Vector2`

## [0.1.4] - 2025-12-22

### Added

- `IntVector2` indexing and thus `pygame.typing.IntPoint` compatibility
- CI: run tests

### Changed

- Replaced `IntVector2.from_tuple()` with `IntVector2.from_point()`
  which takes `pygame.typing.IntPoint`, i.e. a pair of integers
- `IntVector2` add/subtract broadened to take `pygame.typing.IntPoint` 

### Fixed

- `pdoc` was a runtime instead of dev dependency
- CI: Python 3.12 was always used, not version from matrix 

## [0.1.3] - 2025-12-05

### Added

- `geometry.relative_bearing()`

### Changed

- `Grid.DIRECTIONS` is now a list ordered by rotation, instead of set
- Improved error message on attempting `IntVector2` operations when != 2 elements

## [0.1.2] - 2025-11-30

### Added

- `Grid` class
- `IntVector2.__rmul__()`

## [0.1.1] - 2025-11-24

### Added

- `IntVector2.__len__()`, `__radd__()`, `__rsub__()`
- Raise error on `IntVector2` operations when != 2 elements

## [0.1.0] - 2025-11-14

Initial release

[UNRELEASED]: https://github.com/recreational-projects/flatlandian/compare/v0.1.3...HEAD
[0.1.4]: https://github.com/recreational-projects/flatlandian/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/recreational-projects/flatlandian/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/recreational-projects/flatlandian/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/recreational-projects/flatlandian/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/recreational-projects/flatlandian/releases/tag/v0.1.0