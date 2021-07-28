#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TuitionISVResult import TuitionISVResult
from alipay.aop.api.domain.TuitionISVSchoolDTO import TuitionISVSchoolDTO


class AlipayOverseasOpenSchoolQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenSchoolQueryResponse, self).__init__()
        self._result = None
        self._school_list = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, TuitionISVResult):
            self._result = value
        else:
            self._result = TuitionISVResult.from_alipay_dict(value)
    @property
    def school_list(self):
        return self._school_list

    @school_list.setter
    def school_list(self, value):
        if isinstance(value, TuitionISVSchoolDTO):
            self._school_list = value
        else:
            self._school_list = TuitionISVSchoolDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasOpenSchoolQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'school_list' in response:
            self.school_list = response['school_list']
