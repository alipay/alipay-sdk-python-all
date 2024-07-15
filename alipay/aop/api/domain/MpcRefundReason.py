#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcRefundReason(object):

    def __init__(self):
        self._proof_required = None
        self._reason_text_id = None
        self._reason_tips = None
        self._refund_desc_required = None

    @property
    def proof_required(self):
        return self._proof_required

    @proof_required.setter
    def proof_required(self, value):
        self._proof_required = value
    @property
    def reason_text_id(self):
        return self._reason_text_id

    @reason_text_id.setter
    def reason_text_id(self, value):
        self._reason_text_id = value
    @property
    def reason_tips(self):
        return self._reason_tips

    @reason_tips.setter
    def reason_tips(self, value):
        self._reason_tips = value
    @property
    def refund_desc_required(self):
        return self._refund_desc_required

    @refund_desc_required.setter
    def refund_desc_required(self, value):
        self._refund_desc_required = value


    def to_alipay_dict(self):
        params = dict()
        if self.proof_required:
            if hasattr(self.proof_required, 'to_alipay_dict'):
                params['proof_required'] = self.proof_required.to_alipay_dict()
            else:
                params['proof_required'] = self.proof_required
        if self.reason_text_id:
            if hasattr(self.reason_text_id, 'to_alipay_dict'):
                params['reason_text_id'] = self.reason_text_id.to_alipay_dict()
            else:
                params['reason_text_id'] = self.reason_text_id
        if self.reason_tips:
            if hasattr(self.reason_tips, 'to_alipay_dict'):
                params['reason_tips'] = self.reason_tips.to_alipay_dict()
            else:
                params['reason_tips'] = self.reason_tips
        if self.refund_desc_required:
            if hasattr(self.refund_desc_required, 'to_alipay_dict'):
                params['refund_desc_required'] = self.refund_desc_required.to_alipay_dict()
            else:
                params['refund_desc_required'] = self.refund_desc_required
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcRefundReason()
        if 'proof_required' in d:
            o.proof_required = d['proof_required']
        if 'reason_text_id' in d:
            o.reason_text_id = d['reason_text_id']
        if 'reason_tips' in d:
            o.reason_tips = d['reason_tips']
        if 'refund_desc_required' in d:
            o.refund_desc_required = d['refund_desc_required']
        return o


