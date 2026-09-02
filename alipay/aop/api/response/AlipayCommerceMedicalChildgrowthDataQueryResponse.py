#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConsultantChildInfoVO import ConsultantChildInfoVO
from alipay.aop.api.domain.ConsultantGrowthRecordVO import ConsultantGrowthRecordVO
from alipay.aop.api.domain.ConsultantInterpretVO import ConsultantInterpretVO
from alipay.aop.api.domain.ConsultantStandardDataVO import ConsultantStandardDataVO


class AlipayCommerceMedicalChildgrowthDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalChildgrowthDataQueryResponse, self).__init__()
        self._child_info = None
        self._ext_info = None
        self._growth_records = None
        self._latest_interpret = None
        self._national_standard = None

    @property
    def child_info(self):
        return self._child_info

    @child_info.setter
    def child_info(self, value):
        if isinstance(value, ConsultantChildInfoVO):
            self._child_info = value
        else:
            self._child_info = ConsultantChildInfoVO.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def growth_records(self):
        return self._growth_records

    @growth_records.setter
    def growth_records(self, value):
        if isinstance(value, list):
            self._growth_records = list()
            for i in value:
                if isinstance(i, ConsultantGrowthRecordVO):
                    self._growth_records.append(i)
                else:
                    self._growth_records.append(ConsultantGrowthRecordVO.from_alipay_dict(i))
    @property
    def latest_interpret(self):
        return self._latest_interpret

    @latest_interpret.setter
    def latest_interpret(self, value):
        if isinstance(value, ConsultantInterpretVO):
            self._latest_interpret = value
        else:
            self._latest_interpret = ConsultantInterpretVO.from_alipay_dict(value)
    @property
    def national_standard(self):
        return self._national_standard

    @national_standard.setter
    def national_standard(self, value):
        if isinstance(value, ConsultantStandardDataVO):
            self._national_standard = value
        else:
            self._national_standard = ConsultantStandardDataVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalChildgrowthDataQueryResponse, self).parse_response_content(response_content)
        if 'child_info' in response:
            self.child_info = response['child_info']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'growth_records' in response:
            self.growth_records = response['growth_records']
        if 'latest_interpret' in response:
            self.latest_interpret = response['latest_interpret']
        if 'national_standard' in response:
            self.national_standard = response['national_standard']
