#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreativeStyle import CreativeStyle


class AlipayDigitalopUcdpApecreativeStyleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalopUcdpApecreativeStyleQueryResponse, self).__init__()
        self._creative_styles = None

    @property
    def creative_styles(self):
        return self._creative_styles

    @creative_styles.setter
    def creative_styles(self, value):
        if isinstance(value, list):
            self._creative_styles = list()
            for i in value:
                if isinstance(i, CreativeStyle):
                    self._creative_styles.append(i)
                else:
                    self._creative_styles.append(CreativeStyle.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalopUcdpApecreativeStyleQueryResponse, self).parse_response_content(response_content)
        if 'creative_styles' in response:
            self.creative_styles = response['creative_styles']
