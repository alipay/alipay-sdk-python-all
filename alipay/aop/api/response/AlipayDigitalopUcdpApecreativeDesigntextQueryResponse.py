#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemDesignTextInfo import ItemDesignTextInfo


class AlipayDigitalopUcdpApecreativeDesigntextQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalopUcdpApecreativeDesigntextQueryResponse, self).__init__()
        self._item_design_text_info_list = None

    @property
    def item_design_text_info_list(self):
        return self._item_design_text_info_list

    @item_design_text_info_list.setter
    def item_design_text_info_list(self, value):
        if isinstance(value, list):
            self._item_design_text_info_list = list()
            for i in value:
                if isinstance(i, ItemDesignTextInfo):
                    self._item_design_text_info_list.append(i)
                else:
                    self._item_design_text_info_list.append(ItemDesignTextInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalopUcdpApecreativeDesigntextQueryResponse, self).parse_response_content(response_content)
        if 'item_design_text_info_list' in response:
            self.item_design_text_info_list = response['item_design_text_info_list']
