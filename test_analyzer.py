import pytest
import os
from scripts.calculate_stats import FastqAnalyzer

def test_get_gc_content():
    """Unit Test: Checks if GC content is calculated correctly."""
    assert FastqAnalyzer.get_gc_content("ATGC") == 50.0
    assert FastqAnalyzer.get_gc_content("") == 0.0

def test_get_mean_quality():
    """Unit Test: Checks if mean quality is calculated correctly."""
    assert FastqAnalyzer.get_mean_quality([10, 20, 30]) == 20.0
    assert FastqAnalyzer.get_mean_quality([]) == 0.0

def test_missing_file():
    """Requirement Test: Should raise FileNotFoundError for a missing file."""
    analyzer = FastqAnalyzer("non_existent_file.fastq")
    with pytest.raises(FileNotFoundError):
        analyzer.analyze()

def test_empty_fastq_file(tmp_path):
    """Requirement Test: Should raise ValueError if the file is completely empty."""
    empty_file = tmp_path / "empty_file.fastq"
    empty_file.write_text("") 
    
    analyzer = FastqAnalyzer(str(empty_file))
    with pytest.raises(ValueError, match="completely empty"):
        analyzer.analyze()

def test_invalid_fastq_content(tmp_path):
    """Requirement Test: Should raise ValueError for non-FASTQ formats."""
    invalid_file = tmp_path / "invalid.fastq"
    invalid_file.write_text("This is not a FASTQ sequence, just random text.")
    
    analyzer = FastqAnalyzer(str(invalid_file))
    # Hatayı garantiye almak için Biopython'un kendi mesajını birebir yazdık:
    with pytest.raises(ValueError, match="Records in Fastq files should start with '@' character"):
        analyzer.analyze()