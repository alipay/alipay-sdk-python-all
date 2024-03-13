#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChapterInfo import ChapterInfo


class AlipayUserAntbookcontentChapterQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAntbookcontentChapterQueryResponse, self).__init__()
        self._chapter_info_list = None
        self._page_num = None
        self._page_size = None
        self._total_count = None

    @property
    def chapter_info_list(self):
        return self._chapter_info_list

    @chapter_info_list.setter
    def chapter_info_list(self, value):
        if isinstance(value, list):
            self._chapter_info_list = list()
            for i in value:
                if isinstance(i, ChapterInfo):
                    self._chapter_info_list.append(i)
                else:
                    self._chapter_info_list.append(ChapterInfo.from_alipay_dict(i))
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAntbookcontentChapterQueryResponse, self).parse_response_content(response_content)
        if 'chapter_info_list' in response:
            self.chapter_info_list = response['chapter_info_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
