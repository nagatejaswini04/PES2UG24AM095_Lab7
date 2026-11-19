from hypothesis import given, strategies as st
import pytest
import re

from student_grades import average_marks, parse_srn, short_name


@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1).map(
    lambda values: ",".join(map(str, values))))
def test_average_marks_valid_csv_returns_average(csv):
    values = [int(value) for value in csv.split(",")]
    assert average_marks(csv) == round(sum(values) / len(values), 2)


@given(st.text().filter(lambda value: not value.strip()))
def test_average_marks_rejects_empty_input(value):
    with pytest.raises(ValueError):
        average_marks(value)


@given(st.text().filter(lambda value: any(ch.isalpha() for ch in value)))
def test_average_marks_rejects_non_numeric_content(value):
    with pytest.raises(ValueError):
        average_marks(value)


@given(st.lists(st.integers().filter(lambda n: n < 0 or n > 100), min_size=1)
       .map(lambda values: ",".join(map(str, values))))
def test_average_marks_rejects_out_of_range_marks(csv):
    with pytest.raises(ValueError):
        average_marks(csv)


@given(st.integers(min_value=1, max_value=3), st.integers(min_value=0, max_value=99),
       st.sampled_from(["CS", "AM", "AI", "ME", "EC"]))
def test_parse_srn_extracts_fields(campus, year, dept):
    srn = f"PES{campus}UG{year:02d}{dept}123"
    assert parse_srn(srn) == (f"PES{campus}", year, dept)


@given(st.text().filter(lambda value: not re.fullmatch(r"PES[1-3]UG\d{2}[A-Z]{2}\d{3}", value)))
def test_parse_srn_rejects_malformed_strings(value):
    with pytest.raises(ValueError):
        parse_srn(value)


@given(st.lists(st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu")),
                        min_size=1, max_size=12), min_size=2, max_size=8))
def test_short_name_uses_first_initial_and_last_word(parts):
    full_name = " ".join(parts)
    expected = parts[0][0].upper() + ". " + parts[-1].capitalize()
    assert short_name(full_name) == expected


@given(st.text().filter(lambda value: len(value.split()) < 2))
def test_short_name_rejects_single_or_empty_name(value):
    with pytest.raises(ValueError):
        short_name(value)


@given(st.one_of(st.none(), st.integers(), st.lists(st.text())))
def test_all_functions_reject_non_string_inputs(value):
    with pytest.raises(TypeError):
        average_marks(value)
    with pytest.raises(TypeError):
        parse_srn(value)
    with pytest.raises(TypeError):
        short_name(value)
