#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JASchoolEntityInfo import JASchoolEntityInfo


class AlipayFundJointaccountSchoolAccountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountSchoolAccountConsultResponse, self).__init__()
        self._has_registered = None
        self._school_entity_info_list = None

    @property
    def has_registered(self):
        return self._has_registered

    @has_registered.setter
    def has_registered(self, value):
        self._has_registered = value
    @property
    def school_entity_info_list(self):
        return self._school_entity_info_list

    @school_entity_info_list.setter
    def school_entity_info_list(self, value):
        if isinstance(value, list):
            self._school_entity_info_list = list()
            for i in value:
                if isinstance(i, JASchoolEntityInfo):
                    self._school_entity_info_list.append(i)
                else:
                    self._school_entity_info_list.append(JASchoolEntityInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountSchoolAccountConsultResponse, self).parse_response_content(response_content)
        if 'has_registered' in response:
            self.has_registered = response['has_registered']
        if 'school_entity_info_list' in response:
            self.school_entity_info_list = response['school_entity_info_list']
