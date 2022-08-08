#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FormTemplateRelationDTO import FormTemplateRelationDTO


class DatadigitalFincloudFinsaasFormtemplateRelationsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasFormtemplateRelationsBatchqueryResponse, self).__init__()
        self._form_template_relations = None
        self._total = None

    @property
    def form_template_relations(self):
        return self._form_template_relations

    @form_template_relations.setter
    def form_template_relations(self, value):
        if isinstance(value, list):
            self._form_template_relations = list()
            for i in value:
                if isinstance(i, FormTemplateRelationDTO):
                    self._form_template_relations.append(i)
                else:
                    self._form_template_relations.append(FormTemplateRelationDTO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasFormtemplateRelationsBatchqueryResponse, self).parse_response_content(response_content)
        if 'form_template_relations' in response:
            self.form_template_relations = response['form_template_relations']
        if 'total' in response:
            self.total = response['total']
