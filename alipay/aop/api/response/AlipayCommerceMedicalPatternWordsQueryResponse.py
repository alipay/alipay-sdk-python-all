#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PatternWord import PatternWord


class AlipayCommerceMedicalPatternWordsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPatternWordsQueryResponse, self).__init__()
        self._pattern_words = None

    @property
    def pattern_words(self):
        return self._pattern_words

    @pattern_words.setter
    def pattern_words(self, value):
        if isinstance(value, list):
            self._pattern_words = list()
            for i in value:
                if isinstance(i, PatternWord):
                    self._pattern_words.append(i)
                else:
                    self._pattern_words.append(PatternWord.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPatternWordsQueryResponse, self).parse_response_content(response_content)
        if 'pattern_words' in response:
            self.pattern_words = response['pattern_words']
