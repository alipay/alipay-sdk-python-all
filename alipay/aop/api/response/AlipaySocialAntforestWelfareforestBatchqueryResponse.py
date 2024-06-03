#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WelfareForestDetailDTO import WelfareForestDetailDTO


class AlipaySocialAntforestWelfareforestBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestWelfareforestBatchqueryResponse, self).__init__()
        self._global_display_info = None
        self._welfare_forest_detail_list = None

    @property
    def global_display_info(self):
        return self._global_display_info

    @global_display_info.setter
    def global_display_info(self, value):
        self._global_display_info = value
    @property
    def welfare_forest_detail_list(self):
        return self._welfare_forest_detail_list

    @welfare_forest_detail_list.setter
    def welfare_forest_detail_list(self, value):
        if isinstance(value, list):
            self._welfare_forest_detail_list = list()
            for i in value:
                if isinstance(i, WelfareForestDetailDTO):
                    self._welfare_forest_detail_list.append(i)
                else:
                    self._welfare_forest_detail_list.append(WelfareForestDetailDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestWelfareforestBatchqueryResponse, self).parse_response_content(response_content)
        if 'global_display_info' in response:
            self.global_display_info = response['global_display_info']
        if 'welfare_forest_detail_list' in response:
            self.welfare_forest_detail_list = response['welfare_forest_detail_list']
