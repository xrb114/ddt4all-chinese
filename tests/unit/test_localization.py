from pathlib import Path

import polib

from ddt4all import options


def test_simplified_chinese_is_selectable_and_translated():
    """The source catalog must be complete and usable by the build process."""
    assert options.lang_list["简体中文"] == "zh_CN"

    catalog = (
        Path(options.BASE_DIR).parents[1]
        / "locales"
        / "zh_CN"
        / "LC_MESSAGES"
        / "ddt4all.po"
    )
    translation = polib.pofile(catalog)

    assert not [entry for entry in translation if "fuzzy" in entry.flags]
    assert all(entry.msgstr for entry in translation)
    assert translation.find("DoIP request failed: %s").msgstr == "DoIP 请求失败：%s"
    assert translation.find("Diagnostic Trouble Codes").msgstr == "诊断故障码 (DTC)"
