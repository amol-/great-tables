from typing import Optional, Union, List, Any

default_fonts_list = [
    "-apple-system",
    "BlinkMacSystemFont",
    "Segoe UI",
    "Roboto",
    "Oxygen",
    "Ubuntu",
    "Cantarell",
    "Helvetica Neue",
    "Fira Sans",
    "Droid Sans",
    "Arial",
    "sans-serif",
]


class OptionsInfo:
    parameter: Optional[str]
    scss: Optional[bool]
    category: Optional[str]
    type: Optional[str]
    value: Optional[Union[Any, List[str]]]

    def __init__(
        self,
        parameter: Optional[str] = None,
        scss: Optional[bool] = None,
        category: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[Union[Any, List[str]]] = None,
    ):
        self.parameter = parameter
        self.scss = scss
        self.category = category
        self.type = type
        self.value = value


# fmt: off
class Options:
    def __init__(self):
        self._options: list[OptionsInfo] = [
            #           parameter                            scss    category            type        value
            OptionsInfo("container_width",                   False,  "container",        "px",       "auto"),
            OptionsInfo("container_height",                  False,  "container",        "px",       "auto"),
            OptionsInfo("container_overflow_x",              False,  "container",        "overflow", "auto"),
            OptionsInfo("container_overflow_y",              False,  "container",        "overflow", "auto"),
            OptionsInfo("table_id",                          False,  "table",            "value",    None),
            OptionsInfo("table_caption",                     False,  "table",            "value",    None),
            OptionsInfo("table_width",                        True,  "table",            "px",       "auto"),
            OptionsInfo("table_layout",                       True,  "table",            "value",    "fixed"),
            OptionsInfo("table_margin_left",                  True,  "table",            "px",       "auto"),
            OptionsInfo("table_margin_right",                 True,  "table",            "px",       "auto"),
            OptionsInfo("table_background_color",             True,  "table",            "value",    "#FFFFFF"),
            OptionsInfo("table_additional_css",              False,  "table",            "values",   None),
            OptionsInfo("table_font_names",                  False,  "table",            "values",   default_fonts_list),
            OptionsInfo("table_font_size",                    True,  "table",            "px",       "16px"),
            OptionsInfo("table_font_weight",                  True,  "table",            "value",    "normal"),
            OptionsInfo("table_font_style",                   True,  "table",            "value",    "normal"),
            OptionsInfo("table_font_color",                   True,  "table",            "value",    "#333333"),
            OptionsInfo("table_font_color_light",             True,  "table",            "value",    "#FFFFFF"),
            OptionsInfo("table_border_top_include",          False,  "table",            "logical",  True),
            OptionsInfo("table_border_top_style",             True,  "table",            "value",    "solid"),
            OptionsInfo("table_border_top_width",             True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_top_color",             True,  "table",            "value",    "#A8A8A8"),
            OptionsInfo("table_border_right_style",           True,  "table",            "value",    "none"),
            OptionsInfo("table_border_right_width",           True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_right_color",           True,  "table",            "value",    "#D3D3D3"),
            OptionsInfo("table_border_bottom_include",       False,  "table",            "logical",  True),
            OptionsInfo("table_border_bottom_style",          True,  "table",            "value",    "solid"),
            OptionsInfo("table_border_bottom_width",          True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_bottom_color",          True,  "table",            "value",    "#A8A8A8"),
            OptionsInfo("table_border_left_style",            True,  "table",            "value",    "none"),
            OptionsInfo("table_border_left_width",            True,  "table",            "px",       "2px"),
            OptionsInfo("table_border_left_color",            True,  "table",            "value",    "#D3D3D3"),
            OptionsInfo("heading_background_color",           True,  "heading",          "value",    None),
            OptionsInfo("heading_align",                      True,  "heading",          "value",    "center"),
            OptionsInfo("heading_title_font_size",            True,  "heading",          "px",       "125%"),
            OptionsInfo("heading_title_font_weight",          True,  "heading",          "value",    "initial"),
            OptionsInfo("heading_subtitle_font_size",         True,  "heading",          "px",       "85%"),
            OptionsInfo("heading_subtitle_font_weight",       True,  "heading",          "value",    "initial"),
            OptionsInfo("heading_padding",                    True,  "heading",          "px",       "4px"),
            OptionsInfo("heading_padding_horizontal",         True,  "heading",          "px",       "5px"),
            OptionsInfo("heading_border_bottom_style",        True,  "heading",          "value",    "solid"),
            OptionsInfo("heading_border_bottom_width",        True,  "heading",          "px",       "2px"),
            OptionsInfo("heading_border_bottom_color",        True,  "heading",          "value",    "#D3D3D3"),
            OptionsInfo("heading_border_lr_style",            True,  "heading",          "value",    "none"),
            OptionsInfo("heading_border_lr_width",            True,  "heading",          "px",       "1px"),
            OptionsInfo("heading_border_lr_color",            True,  "heading",          "value",    "#D3D3D3"),
            OptionsInfo("column_labels_background_color",     True,  "column_labels",    "value",    None),
            OptionsInfo("column_labels_font_size",            True,  "column_labels",    "px",       "100%"),
            OptionsInfo("column_labels_font_weight",          True,  "column_labels",    "value",    "normal"),
            OptionsInfo("column_labels_text_transform",       True,  "column_labels",    "value",    "inherit"),
            OptionsInfo("column_labels_padding",              True,  "column_labels",    "px",       "5px"),
            OptionsInfo("column_labels_padding_horizontal",   True,  "column_labels",    "px",       "5px"),
            OptionsInfo("column_labels_vlines_style",         True,  "table_body",       "value",    "none"),
            OptionsInfo("column_labels_vlines_width",         True,  "table_body",       "px",       "1px"),
            OptionsInfo("column_labels_vlines_color",         True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("column_labels_border_top_style",     True,  "column_labels",    "value",    "solid"),
            OptionsInfo("column_labels_border_top_width",     True,  "column_labels",    "px",       "2px"),
            OptionsInfo("column_labels_border_top_color",     True,  "column_labels",    "value",    "#D3D3D3"),
            OptionsInfo("column_labels_border_bottom_style",  True,  "column_labels",    "value",    "solid"),
            OptionsInfo("column_labels_border_bottom_width",  True,  "column_labels",    "px",       "2px"),
            OptionsInfo("column_labels_border_bottom_color",  True,  "column_labels",    "value",    "#D3D3D3"),
            OptionsInfo("column_labels_border_lr_style",      True,  "column_labels",    "value",    "none"),
            OptionsInfo("column_labels_border_lr_width",      True,  "column_labels",    "px",       "1px"),
            OptionsInfo("column_labels_border_lr_color",      True,  "column_labels",    "value",    "#D3D3D3"),
            OptionsInfo("column_labels_hidden",              False,  "column_labels",    "logical",  False),
            OptionsInfo("row_group_background_color",         True,  "row_group",        "value",    None),
            OptionsInfo("row_group_font_size",                True,  "row_group",        "px",       "100%"),
            OptionsInfo("row_group_font_weight",              True,  "row_group",        "value",    "initial"),
            OptionsInfo("row_group_text_transform",           True,  "row_group",        "value",    "inherit"),
            OptionsInfo("row_group_padding",                  True,  "row_group",        "px",       "8px"),
            OptionsInfo("row_group_padding_horizontal",       True,  "row_group",        "px",       "5px"),
            OptionsInfo("row_group_border_top_style",         True,  "row_group",        "value",    "solid"),
            OptionsInfo("row_group_border_top_width",         True,  "row_group",        "px",       "2px"),
            OptionsInfo("row_group_border_top_color",         True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_border_right_style",       True,  "row_group",        "value",    "none"),
            OptionsInfo("row_group_border_right_width",       True,  "row_group",        "px",       "1px"),
            OptionsInfo("row_group_border_right_color",       True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_border_bottom_style",      True,  "row_group",        "value",    "solid"),
            OptionsInfo("row_group_border_bottom_width",      True,  "row_group",        "px",       "2px"),
            OptionsInfo("row_group_border_bottom_color",      True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_border_left_style",        True,  "row_group",        "value",    "none"),
            OptionsInfo("row_group_border_left_width",        True,  "row_group",        "px",       "1px"),
            OptionsInfo("row_group_border_left_color",        True,  "row_group",        "value",    "#D3D3D3"),
            OptionsInfo("row_group_default_label",           False,  "row_group",        "value",    None),
            OptionsInfo("row_group_as_column",               False,  "row_group",        "logical",  False),
            OptionsInfo("table_body_hlines_style",            True,  "table_body",       "value",    "solid"),
            OptionsInfo("table_body_hlines_width",            True,  "table_body",       "px",       "1px"),
            OptionsInfo("table_body_hlines_color",            True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("table_body_vlines_style",            True,  "table_body",       "value",    "none"),
            OptionsInfo("table_body_vlines_width",            True,  "table_body",       "px",       "1px"),
            OptionsInfo("table_body_vlines_color",            True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("table_body_border_top_style",        True,  "table_body",       "value",    "solid"),
            OptionsInfo("table_body_border_top_width",        True,  "table_body",       "px",       "2px"),
            OptionsInfo("table_body_border_top_color",        True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("table_body_border_bottom_style",     True,  "table_body",       "value",    "solid"),
            OptionsInfo("table_body_border_bottom_width",     True,  "table_body",       "px",       "2px"),
            OptionsInfo("table_body_border_bottom_color",     True,  "table_body",       "value",    "#D3D3D3"),
            OptionsInfo("data_row_padding",                   True,  "data_row",         "px",       "8px"),
            OptionsInfo("data_row_padding_horizontal",        True,  "data_row",         "px",       "5px"),
            OptionsInfo("stub_background_color",              True,  "stub",             "value",    None),
            OptionsInfo("stub_font_size",                     True,  "stub",             "px",       "100%"),
            OptionsInfo("stub_font_weight",                   True,  "stub",             "value",    "initial"),
            OptionsInfo("stub_text_transform",                True,  "stub",             "value",    "inherit"),
            OptionsInfo("stub_border_style",                  True,  "stub",             "value",    "solid"),
            OptionsInfo("stub_border_width",                  True,  "stub",             "px",       "2px"),
            OptionsInfo("stub_border_color",                  True,  "stub",             "value",    "#D3D3D3"),
            OptionsInfo("stub_row_group_background_color",    True,  "stub",             "value",    None),
            OptionsInfo("stub_row_group_font_size",           True,  "stub",             "px",       "100%"),
            OptionsInfo("stub_row_group_font_weight",         True,  "stub",             "value",    "initial"),
            OptionsInfo("stub_row_group_text_transform",      True,  "stub",             "value",    "inherit"),
            OptionsInfo("stub_row_group_border_style",        True,  "stub",             "value",    "solid"),
            OptionsInfo("stub_row_group_border_width",        True,  "stub",             "px",       "2px"),
            OptionsInfo("stub_row_group_border_color",        True,  "stub",             "value",    "#D3D3D3"),
            OptionsInfo("summary_row_padding",                True,  "summary_row",      "px",       "8px"),
            OptionsInfo("summary_row_padding_horizontal",     True,  "summary_row",      "px",       "5px"),
            OptionsInfo("summary_row_background_color",       True,  "summary_row",      "value",    None),
            OptionsInfo("summary_row_text_transform",         True,  "summary_row",      "value",    "inherit"),
            OptionsInfo("summary_row_border_style",           True,  "summary_row",      "value",    "solid"),
            OptionsInfo("summary_row_border_width",           True,  "summary_row",      "px",       "2px"),
            OptionsInfo("summary_row_border_color",           True,  "summary_row",      "value",    "#D3D3D3"),
            OptionsInfo("grand_summary_row_padding",          True,  "grand_summary_row", "px",      "8px"),
            OptionsInfo("grand_summary_row_padding_horizontal",True, "grand_summary_row", "px",      "5px"),
            OptionsInfo("grand_summary_row_background_color", True,  "grand_summary_row", "value",   None),
            OptionsInfo("grand_summary_row_text_transform",   True,  "grand_summary_row", "value",   "inherit"),
            OptionsInfo("grand_summary_row_border_style",     True,  "grand_summary_row", "value",   "double"),
            OptionsInfo("grand_summary_row_border_width",     True,  "grand_summary_row", "px",      "6px"),
            OptionsInfo("grand_summary_row_border_color",     True,  "grand_summary_row", "value",   "#D3D3D3"),
            OptionsInfo("footnotes_font_size",                True,  "footnotes",        "px",       "90%"),
            OptionsInfo("footnotes_padding",                  True,  "footnotes",        "px",       "4px"),
            OptionsInfo("footnotes_padding_horizontal",       True,  "footnotes",        "px",       "5px"),
            OptionsInfo("footnotes_background_color",         True,  "footnotes",        "value",    None),
            OptionsInfo("footnotes_margin",                   True,  "footnotes",        "px",       "0px"),
            OptionsInfo("footnotes_border_bottom_style",      True,  "footnotes",        "value",    "none"),
            OptionsInfo("footnotes_border_bottom_width",      True,  "footnotes",        "px",       "2px"),
            OptionsInfo("footnotes_border_bottom_color",      True,  "footnotes",        "value",    "#D3D3D3"),
            OptionsInfo("footnotes_border_lr_style",          True,  "footnotes",        "value",    "none"),
            OptionsInfo("footnotes_border_lr_width",          True,  "footnotes",        "px",       "2px"),
            OptionsInfo("footnotes_border_lr_color",          True,  "footnotes",        "value",    "#D3D3D3"),
            OptionsInfo("footnotes_marks" ,                  False,  "footnotes",        "values",   "numbers"),
            OptionsInfo("footnotes_multiline",               False,  "footnotes",        "logical",  True),
            OptionsInfo("footnotes_sep",                     False,  "footnotes",        "value",    " "),
            OptionsInfo("source_notes_padding",               True,  "source_notes",     "px",       "4px"),
            OptionsInfo("source_notes_padding_horizontal",    True,  "source_notes",     "px",       "5px"),
            OptionsInfo("source_notes_background_color",      True,  "source_notes",     "value",    None),
            OptionsInfo("source_notes_font_size",             True,  "source_notes",     "px",       "90%"),
            OptionsInfo("source_notes_border_bottom_style",   True,  "source_notes",     "value",    "none"),
            OptionsInfo("source_notes_border_bottom_width",   True,  "source_notes",     "px",       "2px"),
            OptionsInfo("source_notes_border_bottom_color",   True,  "source_notes",     "value",    "#D3D3D3"),
            OptionsInfo("source_notes_border_lr_style",       True,  "source_notes",     "value",    "none"),
            OptionsInfo("source_notes_border_lr_width",       True,  "source_notes",     "px",       "2px"),
            OptionsInfo("source_notes_border_lr_color",       True,  "source_notes",     "value",    "#D3D3D3"),
            OptionsInfo("source_notes_multiline",            False,  "source_notes",     "logical",  True),
            OptionsInfo("source_notes_sep",                  False,  "source_notes",     "value",    " "),
            OptionsInfo("row_striping_background_color",      True,  "row",              "value",    "rgba(128,128,128,0.05)"),
            OptionsInfo("row_striping_include_stub",         False,  "row",              "logical",  False),
            OptionsInfo("row_striping_include_table_body",   False,  "row",              "logical",  False),
            OptionsInfo("page_orientation",                  False,  "page",             "value",    "portrait"),
            OptionsInfo("page_numbering",                    False,  "page",             "logical",  False),
            OptionsInfo("page_header_use_tbl_headings",      False,  "page",             "logical",  False),
            OptionsInfo("page_footer_use_tbl_notes",         False,  "page",             "logical",  False),
            OptionsInfo("page_width",                        False,  "page",             "value",    "8.5in"),
            OptionsInfo("page_height",                       False,  "page",             "value",    "11.0in"),
            OptionsInfo("page_margin_left",                  False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_right",                 False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_top",                   False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_margin_bottom",                False,  "page",             "value",    "1.0in"),
            OptionsInfo("page_header_height",                False,  "page",             "value",    "0.5in"),
            OptionsInfo("page_footer_height",                False,  "page",             "value",    "0.5in"),
        ]
# fmt: on

    def _get_option_value(self, option: str) -> Union[Any, List[str]]:
        return [x.value for x in self._options if x.parameter == option].pop()
    
    # TODO: create the `_set_option_value()` function

class OptionsAPI:
    _options: Options

    def __init__(self):
        self._options = Options()

    # TODO: create the `tab_options()` function

    # TODO: create the `opt_footnote_marks()` function

    # TODO: create the `opt_row_striping()` function

    # TODO: create the `opt_align_table_header()` function

    # TODO: create the `opt_vertical_padding()` function

    # TODO: create the `opt_horizontal_padding()` function

    # TODO: create the `opt_all_caps()` function

    # TODO: create the `opt_table_lines()` function

    # TODO: create the `opt_table_outline()` function

    # TODO: create the `opt_table_font()` function
    
    # TODO: create the `opt_css()` function
