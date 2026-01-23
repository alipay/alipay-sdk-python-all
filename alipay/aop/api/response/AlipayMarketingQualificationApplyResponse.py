#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QualificationVoucherDTO import QualificationVoucherDTO


class AlipayMarketingQualificationApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingQualificationApplyResponse, self).__init__()
        self._anchor_id = None
        self._anchor_instance_id = None
        self._qual_id = None
        self._qual_instance_id = None
        self._voucher = None

    @property
    def anchor_id(self):
        return self._anchor_id

    @anchor_id.setter
    def anchor_id(self, value):
        self._anchor_id = value
    @property
    def anchor_instance_id(self):
        return self._anchor_instance_id

    @anchor_instance_id.setter
    def anchor_instance_id(self, value):
        self._anchor_instance_id = value
    @property
    def qual_id(self):
        return self._qual_id

    @qual_id.setter
    def qual_id(self, value):
        self._qual_id = value
    @property
    def qual_instance_id(self):
        return self._qual_instance_id

    @qual_instance_id.setter
    def qual_instance_id(self, value):
        self._qual_instance_id = value
    @property
    def voucher(self):
        return self._voucher

    @voucher.setter
    def voucher(self, value):
        if isinstance(value, QualificationVoucherDTO):
            self._voucher = value
        else:
            self._voucher = QualificationVoucherDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingQualificationApplyResponse, self).parse_response_content(response_content)
        if 'anchor_id' in response:
            self.anchor_id = response['anchor_id']
        if 'anchor_instance_id' in response:
            self.anchor_instance_id = response['anchor_instance_id']
        if 'qual_id' in response:
            self.qual_id = response['qual_id']
        if 'qual_instance_id' in response:
            self.qual_instance_id = response['qual_instance_id']
        if 'voucher' in response:
            self.voucher = response['voucher']
