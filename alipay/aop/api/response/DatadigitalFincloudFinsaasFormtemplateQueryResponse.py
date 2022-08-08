#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasFormtemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasFormtemplateQueryResponse, self).__init__()
        self._form_template_id = None
        self._form_template_json_string = None
        self._form_template_name = None

    @property
    def form_template_id(self):
        return self._form_template_id

    @form_template_id.setter
    def form_template_id(self, value):
        self._form_template_id = value
    @property
    def form_template_json_string(self):
        return self._form_template_json_string

    @form_template_json_string.setter
    def form_template_json_string(self, value):
        self._form_template_json_string = value
    @property
    def form_template_name(self):
        return self._form_template_name

    @form_template_name.setter
    def form_template_name(self, value):
        self._form_template_name = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasFormtemplateQueryResponse, self).parse_response_content(response_content)
        if 'form_template_id' in response:
            self.form_template_id = response['form_template_id']
        if 'form_template_json_string' in response:
            self.form_template_json_string = response['form_template_json_string']
        if 'form_template_name' in response:
            self.form_template_name = response['form_template_name']
