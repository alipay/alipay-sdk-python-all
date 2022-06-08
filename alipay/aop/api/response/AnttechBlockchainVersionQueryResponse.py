#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IterationVersionInfoDeliverObj import IterationVersionInfoDeliverObj


class AnttechBlockchainVersionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainVersionQueryResponse, self).__init__()
        self._iteration_version_info_deliver_obj_list = None

    @property
    def iteration_version_info_deliver_obj_list(self):
        return self._iteration_version_info_deliver_obj_list

    @iteration_version_info_deliver_obj_list.setter
    def iteration_version_info_deliver_obj_list(self, value):
        if isinstance(value, list):
            self._iteration_version_info_deliver_obj_list = list()
            for i in value:
                if isinstance(i, IterationVersionInfoDeliverObj):
                    self._iteration_version_info_deliver_obj_list.append(i)
                else:
                    self._iteration_version_info_deliver_obj_list.append(IterationVersionInfoDeliverObj.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainVersionQueryResponse, self).parse_response_content(response_content)
        if 'iteration_version_info_deliver_obj_list' in response:
            self.iteration_version_info_deliver_obj_list = response['iteration_version_info_deliver_obj_list']
