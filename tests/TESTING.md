# Testing Framework Documentation

## Overview
This document describes the comprehensive testing framework for the Number Guessing Game. The framework includes unit tests, integration tests, performance tests, and automated test running capabilities.

## Test Structure

### Test Files
- `tests/test_game_logic.py` - Unit tests for core game logic
- `tests/test_integration.py` - Integration tests for component interaction
- `tests/test_performance.py` - Performance and stress tests
- `tests/__init__.py` - Package initialization for tests

### Configuration Files
- `pytest.ini` - pytest configuration and settings
- `run_tests.py` - Test runner script with various options

## Test Categories

### 1. Unit Tests (`test_game_logic.py`)
Tests individual components and methods in isolation:

- **Game Initialization**: Tests default values and setup
- **Input Validation**: Tests the `sanitize_input()` method
- **Hint Generation**: Tests hint logic for all levels
- **Game Logic**: Tests guess processing and game state
- **Boundary Conditions**: Tests edge cases and limits
- **Error Handling**: Tests invalid input scenarios

### 2. Integration Tests (`test_integration.py`)
Tests interaction between different components:

- **Complete Game Flow**: Full game scenarios from start to finish
- **Multi-round Games**: Tests session management
- **Hint System Integration**: Tests hint system with game flow
- **Strategy Tracking**: Tests the strategy advice system
- **State Consistency**: Tests that game state remains consistent

### 3. Performance Tests (`test_performance.py`)
Tests performance characteristics:

- **Initialization Performance**: Tests startup time
- **Input Processing Speed**: Tests input validation speed
- **Memory Usage**: Tests memory efficiency
- **Concurrent Operations**: Tests thread safety
- **Large Data Handling**: Tests with large datasets

## Running Tests

### Prerequisites
```bash
# Install pytest (if not already installed)
pip install pytest

# Install optional testing dependencies
pip install pytest-html pytest-cov coverage
```

### Basic Test Execution

#### Using pytest directly:
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_game_logic.py

# Run specific test class
pytest tests/test_game_logic.py::TestGuessingGameLogic

# Run specific test method
pytest tests/test_game_logic.py::TestGuessingGameLogic::test_game_initialization
```

#### Using the test runner script:
```bash
# Run all tests
python run_tests.py

# Run only unit tests
python run_tests.py --type unit

# Run with coverage analysis
python run_tests.py --coverage

# Run with verbose output
python run_tests.py --verbose

# Generate HTML report
python run_tests.py --report

# Install test dependencies
python run_tests.py --install-deps
```

### Test Runner Options

The `run_tests.py` script provides several options:

- `--type`: Choose test type (all, unit, integration, performance, fast, slow)
- `--verbose`: Enable verbose output
- `--coverage`: Run with coverage analysis
- `--lint`: Run code linting
- `--report`: Generate HTML test report
- `--install-deps`: Install test dependencies

### Examples

```bash
# Quick test run (exclude slow tests)
python run_tests.py --type fast

# Performance testing only
python run_tests.py --type performance

# Full test suite with coverage
python run_tests.py --type all --coverage --verbose

# Generate comprehensive report
python run_tests.py --report --coverage --lint
```

## Test Patterns and Best Practices

### Mocking Strategy
Tests use extensive mocking to isolate components:

```python
@pytest.fixture
def mock_game(self):
    """Create a mock game instance for testing"""
    with patch('game.ctk.CTk'), \
         patch('game.ctk.CTkLabel'), \
         patch('game.ctk.CTkFrame'):
        
        game = GuessingGameGUI()
        game.messages_text = MagicMock()
        game.guess_entry = MagicMock()
        return game
```

### Test Data Management
Tests use controlled data for consistency:

```python
@patch('random.randint', return_value=42)
def test_correct_guess(self, mock_random, mock_game):
    """Test making a correct guess"""
    # Test implementation
```

### Parameterized Tests
Tests use parameterization for comprehensive coverage:

```python
@pytest.mark.parametrize("input_value,expected_result", [
    ("42", 42),
    ("0", 0),
    ("100", 100),
])
def test_valid_inputs(self, input_value, expected_result, mock_game):
    # Test implementation
```

## Coverage Analysis

### Generating Coverage Reports
```bash
# Terminal coverage report
pytest --cov=game --cov-report=term-missing

# HTML coverage report
pytest --cov=game --cov-report=html

# XML coverage report (for CI/CD)
pytest --cov=game --cov-report=xml
```

### Coverage Targets
- **Overall Coverage**: >90%
- **Critical Functions**: 100%
- **Edge Cases**: 100%
- **Error Handling**: 100%

## Continuous Integration

### GitHub Actions Example
```yaml
name: Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    - name: Run tests
      run: python run_tests.py --coverage
```

## Test Maintenance

### Adding New Tests
1. Identify the component or feature to test
2. Choose the appropriate test file (unit, integration, performance)
3. Write test cases following existing patterns
4. Add appropriate mocking and fixtures
5. Run tests to ensure they pass
6. Update documentation if needed

### Test Naming Conventions
- Test files: `test_*.py`
- Test classes: `Test*`
- Test methods: `test_*`
- Descriptive names: `test_correct_guess_wins_game`

### Fixture Management
```python
@pytest.fixture
def mock_game(self):
    """Reusable game mock for testing"""
    # Setup code
    yield game
    # Teardown code (if needed)
```

## Debugging Tests

### Running Tests in Debug Mode
```bash
# Run with pdb debugger
pytest --pdb

# Run with extra output
pytest -s -v

# Run single test with debugging
pytest -s tests/test_game_logic.py::TestGuessingGameLogic::test_game_initialization
```

### Common Issues and Solutions

1. **Mock Issues**: Ensure all GUI components are properly mocked
2. **Import Errors**: Check that the game module is importable
3. **Random Number Tests**: Use `patch` to control random number generation
4. **Threading Issues**: Use appropriate mocking for threaded operations

## Performance Benchmarking

### Benchmark Tests
Performance tests include benchmarks for:
- Game initialization time
- Input processing speed
- Memory usage patterns
- Concurrent operation handling

### Performance Thresholds
- Initialization: <1 second
- Input processing: <0.1 seconds for 1000 inputs
- Memory usage: Stable across long sessions
- Concurrent operations: <1 second completion

## Reporting and Documentation

### Test Reports
- HTML reports with detailed results
- Coverage reports with line-by-line analysis
- Performance benchmarks with timing data
- Error summaries with stack traces

### Documentation Updates
- Update this document when adding new test categories
- Document any new testing patterns or conventions
- Include examples of complex test scenarios
- Maintain troubleshooting guide

## Future Enhancements

### Planned Improvements
- [ ] Add property-based testing with Hypothesis
- [ ] Implement visual regression testing
- [ ] Add load testing scenarios
- [ ] Create automated test data generation
- [ ] Implement mutation testing
- [ ] Add security testing components

### Integration Opportunities
- [ ] IDE integration for test running
- [ ] Automated test generation from code changes
- [ ] Performance regression detection
- [ ] Test result analytics and trends
