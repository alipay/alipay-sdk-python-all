#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreativeDesignInfo import CreativeDesignInfo
from alipay.aop.api.domain.CreativeDesignInfo import CreativeDesignInfo


class AlipayDigitalopUcdpApecreativeStyledesignrelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalopUcdpApecreativeStyledesignrelationQueryResponse, self).__init__()
        self._creative_design_info_list = None
        self._select_design_info_list = None

    @property
    def creative_design_info_list(self):
        return self._creative_design_info_list

    @creative_design_info_list.setter
    def creative_design_info_list(self, value):
        if isinstance(value, CreativeDesignInfo):
            self._creative_design_info_list = value
        else:
            self._creative_design_info_list = CreativeDesignInfo.from_alipay_dict(value)
    @property
    def select_design_info_list(self):
        return self._select_design_info_list

    @select_design_info_list.setter
    def select_design_info_list(self, value):
        if isinstance(value, list):
            self._select_design_info_list = list()
            for i in value:
                if isinstance(i, CreativeDesignInfo):
                    self._select_design_info_list.append(i)
                else:
                    self._select_design_info_list.append(CreativeDesignInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalopUcdpApecreativeStyledesignrelationQueryResponse, self).parse_response_content(response_content)
        if 'creative_design_info_list' in response:
            self.creative_design_info_list = response['creative_design_info_list']
        if 'select_design_info_list' in response:
            self.select_design_info_list = response['select_design_info_list']
