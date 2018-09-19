#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.McardTemplate import McardTemplate


class AlipayMarketingCardTemplateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardTemplateBatchqueryResponse, self).__init__()
        self._mcard_template = None
        self._template_total = None

    @property
    def mcard_template(self):
        return self._mcard_template

    @mcard_template.setter
    def mcard_template(self, value):
        if isinstance(value, list):
            self._mcard_template = list()
            for i in value:
                if isinstance(i, McardTemplate):
                    self._mcard_template.append(i)
                else:
                    self._mcard_template.append(McardTemplate.from_alipay_dict(i))
    @property
    def template_total(self):
        return self._template_total

    @template_total.setter
    def template_total(self, value):
        self._template_total = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardTemplateBatchqueryResponse, self).parse_response_content(response_content)
        if 'mcard_template' in response:
            self.mcard_template = response['mcard_template']
        if 'template_total' in response:
            self.template_total = response['template_total']
