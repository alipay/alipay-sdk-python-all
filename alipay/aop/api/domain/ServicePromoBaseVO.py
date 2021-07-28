#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoContentBizVO import PromoContentBizVO


class ServicePromoBaseVO(object):

    def __init__(self):
        self._biz_status = None
        self._promo_booth_id = None
        self._promo_contents = None
        self._promo_entity_codes = None
        self._promo_entity_type = None
        self._promo_record_id = None
        self._reject_reason = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def promo_booth_id(self):
        return self._promo_booth_id

    @promo_booth_id.setter
    def promo_booth_id(self, value):
        self._promo_booth_id = value
    @property
    def promo_contents(self):
        return self._promo_contents

    @promo_contents.setter
    def promo_contents(self, value):
        if isinstance(value, list):
            self._promo_contents = list()
            for i in value:
                if isinstance(i, PromoContentBizVO):
                    self._promo_contents.append(i)
                else:
                    self._promo_contents.append(PromoContentBizVO.from_alipay_dict(i))
    @property
    def promo_entity_codes(self):
        return self._promo_entity_codes

    @promo_entity_codes.setter
    def promo_entity_codes(self, value):
        if isinstance(value, list):
            self._promo_entity_codes = list()
            for i in value:
                self._promo_entity_codes.append(i)
    @property
    def promo_entity_type(self):
        return self._promo_entity_type

    @promo_entity_type.setter
    def promo_entity_type(self, value):
        self._promo_entity_type = value
    @property
    def promo_record_id(self):
        return self._promo_record_id

    @promo_record_id.setter
    def promo_record_id(self, value):
        self._promo_record_id = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.promo_booth_id:
            if hasattr(self.promo_booth_id, 'to_alipay_dict'):
                params['promo_booth_id'] = self.promo_booth_id.to_alipay_dict()
            else:
                params['promo_booth_id'] = self.promo_booth_id
        if self.promo_contents:
            if isinstance(self.promo_contents, list):
                for i in range(0, len(self.promo_contents)):
                    element = self.promo_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_contents[i] = element.to_alipay_dict()
            if hasattr(self.promo_contents, 'to_alipay_dict'):
                params['promo_contents'] = self.promo_contents.to_alipay_dict()
            else:
                params['promo_contents'] = self.promo_contents
        if self.promo_entity_codes:
            if isinstance(self.promo_entity_codes, list):
                for i in range(0, len(self.promo_entity_codes)):
                    element = self.promo_entity_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_entity_codes[i] = element.to_alipay_dict()
            if hasattr(self.promo_entity_codes, 'to_alipay_dict'):
                params['promo_entity_codes'] = self.promo_entity_codes.to_alipay_dict()
            else:
                params['promo_entity_codes'] = self.promo_entity_codes
        if self.promo_entity_type:
            if hasattr(self.promo_entity_type, 'to_alipay_dict'):
                params['promo_entity_type'] = self.promo_entity_type.to_alipay_dict()
            else:
                params['promo_entity_type'] = self.promo_entity_type
        if self.promo_record_id:
            if hasattr(self.promo_record_id, 'to_alipay_dict'):
                params['promo_record_id'] = self.promo_record_id.to_alipay_dict()
            else:
                params['promo_record_id'] = self.promo_record_id
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServicePromoBaseVO()
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'promo_booth_id' in d:
            o.promo_booth_id = d['promo_booth_id']
        if 'promo_contents' in d:
            o.promo_contents = d['promo_contents']
        if 'promo_entity_codes' in d:
            o.promo_entity_codes = d['promo_entity_codes']
        if 'promo_entity_type' in d:
            o.promo_entity_type = d['promo_entity_type']
        if 'promo_record_id' in d:
            o.promo_record_id = d['promo_record_id']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        return o


