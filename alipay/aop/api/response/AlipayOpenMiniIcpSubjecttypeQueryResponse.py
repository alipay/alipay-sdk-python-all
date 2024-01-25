#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IcpSubjectTypeList import IcpSubjectTypeList


class AlipayOpenMiniIcpSubjecttypeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIcpSubjecttypeQueryResponse, self).__init__()
        self._subject_types = None

    @property
    def subject_types(self):
        return self._subject_types

    @subject_types.setter
    def subject_types(self, value):
        if isinstance(value, list):
            self._subject_types = list()
            for i in value:
                if isinstance(i, IcpSubjectTypeList):
                    self._subject_types.append(i)
                else:
                    self._subject_types.append(IcpSubjectTypeList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIcpSubjecttypeQueryResponse, self).parse_response_content(response_content)
        if 'subject_types' in response:
            self.subject_types = response['subject_types']
