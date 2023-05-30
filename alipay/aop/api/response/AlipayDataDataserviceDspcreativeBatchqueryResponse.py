#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DspCreativeAuditResult import DspCreativeAuditResult


class AlipayDataDataserviceDspcreativeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceDspcreativeBatchqueryResponse, self).__init__()
        self._creative_audit_result = None

    @property
    def creative_audit_result(self):
        return self._creative_audit_result

    @creative_audit_result.setter
    def creative_audit_result(self, value):
        if isinstance(value, list):
            self._creative_audit_result = list()
            for i in value:
                if isinstance(i, DspCreativeAuditResult):
                    self._creative_audit_result.append(i)
                else:
                    self._creative_audit_result.append(DspCreativeAuditResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceDspcreativeBatchqueryResponse, self).parse_response_content(response_content)
        if 'creative_audit_result' in response:
            self.creative_audit_result = response['creative_audit_result']
