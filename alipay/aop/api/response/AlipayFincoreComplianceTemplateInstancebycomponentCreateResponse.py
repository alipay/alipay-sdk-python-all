#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AgmTemplateInstanceDTO import AgmTemplateInstanceDTO


class AlipayFincoreComplianceTemplateInstancebycomponentCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceTemplateInstancebycomponentCreateResponse, self).__init__()
        self._biz_business_id = None
        self._status = None
        self._template_instances = None

    @property
    def biz_business_id(self):
        return self._biz_business_id

    @biz_business_id.setter
    def biz_business_id(self, value):
        self._biz_business_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_instances(self):
        return self._template_instances

    @template_instances.setter
    def template_instances(self, value):
        if isinstance(value, list):
            self._template_instances = list()
            for i in value:
                if isinstance(i, AgmTemplateInstanceDTO):
                    self._template_instances.append(i)
                else:
                    self._template_instances.append(AgmTemplateInstanceDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceTemplateInstancebycomponentCreateResponse, self).parse_response_content(response_content)
        if 'biz_business_id' in response:
            self.biz_business_id = response['biz_business_id']
        if 'status' in response:
            self.status = response['status']
        if 'template_instances' in response:
            self.template_instances = response['template_instances']
