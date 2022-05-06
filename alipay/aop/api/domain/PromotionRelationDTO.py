#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromotionRelationDTO(object):

    def __init__(self):
        self._apply_reason = None
        self._commodity_id = None
        self._commodity_name = None
        self._create_time = None
        self._promoter_contact_name = None
        self._promoter_contact_phone = None
        self._promoter_name = None
        self._promoter_pid = None
        self._promotion_id = None
        self._promotion_name = None

    @property
    def apply_reason(self):
        return self._apply_reason

    @apply_reason.setter
    def apply_reason(self, value):
        self._apply_reason = value
    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def commodity_name(self):
        return self._commodity_name

    @commodity_name.setter
    def commodity_name(self, value):
        self._commodity_name = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def promoter_contact_name(self):
        return self._promoter_contact_name

    @promoter_contact_name.setter
    def promoter_contact_name(self, value):
        self._promoter_contact_name = value
    @property
    def promoter_contact_phone(self):
        return self._promoter_contact_phone

    @promoter_contact_phone.setter
    def promoter_contact_phone(self, value):
        self._promoter_contact_phone = value
    @property
    def promoter_name(self):
        return self._promoter_name

    @promoter_name.setter
    def promoter_name(self, value):
        self._promoter_name = value
    @property
    def promoter_pid(self):
        return self._promoter_pid

    @promoter_pid.setter
    def promoter_pid(self, value):
        self._promoter_pid = value
    @property
    def promotion_id(self):
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, value):
        self._promotion_id = value
    @property
    def promotion_name(self):
        return self._promotion_name

    @promotion_name.setter
    def promotion_name(self, value):
        self._promotion_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_reason:
            if hasattr(self.apply_reason, 'to_alipay_dict'):
                params['apply_reason'] = self.apply_reason.to_alipay_dict()
            else:
                params['apply_reason'] = self.apply_reason
        if self.commodity_id:
            if hasattr(self.commodity_id, 'to_alipay_dict'):
                params['commodity_id'] = self.commodity_id.to_alipay_dict()
            else:
                params['commodity_id'] = self.commodity_id
        if self.commodity_name:
            if hasattr(self.commodity_name, 'to_alipay_dict'):
                params['commodity_name'] = self.commodity_name.to_alipay_dict()
            else:
                params['commodity_name'] = self.commodity_name
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.promoter_contact_name:
            if hasattr(self.promoter_contact_name, 'to_alipay_dict'):
                params['promoter_contact_name'] = self.promoter_contact_name.to_alipay_dict()
            else:
                params['promoter_contact_name'] = self.promoter_contact_name
        if self.promoter_contact_phone:
            if hasattr(self.promoter_contact_phone, 'to_alipay_dict'):
                params['promoter_contact_phone'] = self.promoter_contact_phone.to_alipay_dict()
            else:
                params['promoter_contact_phone'] = self.promoter_contact_phone
        if self.promoter_name:
            if hasattr(self.promoter_name, 'to_alipay_dict'):
                params['promoter_name'] = self.promoter_name.to_alipay_dict()
            else:
                params['promoter_name'] = self.promoter_name
        if self.promoter_pid:
            if hasattr(self.promoter_pid, 'to_alipay_dict'):
                params['promoter_pid'] = self.promoter_pid.to_alipay_dict()
            else:
                params['promoter_pid'] = self.promoter_pid
        if self.promotion_id:
            if hasattr(self.promotion_id, 'to_alipay_dict'):
                params['promotion_id'] = self.promotion_id.to_alipay_dict()
            else:
                params['promotion_id'] = self.promotion_id
        if self.promotion_name:
            if hasattr(self.promotion_name, 'to_alipay_dict'):
                params['promotion_name'] = self.promotion_name.to_alipay_dict()
            else:
                params['promotion_name'] = self.promotion_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromotionRelationDTO()
        if 'apply_reason' in d:
            o.apply_reason = d['apply_reason']
        if 'commodity_id' in d:
            o.commodity_id = d['commodity_id']
        if 'commodity_name' in d:
            o.commodity_name = d['commodity_name']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'promoter_contact_name' in d:
            o.promoter_contact_name = d['promoter_contact_name']
        if 'promoter_contact_phone' in d:
            o.promoter_contact_phone = d['promoter_contact_phone']
        if 'promoter_name' in d:
            o.promoter_name = d['promoter_name']
        if 'promoter_pid' in d:
            o.promoter_pid = d['promoter_pid']
        if 'promotion_id' in d:
            o.promotion_id = d['promotion_id']
        if 'promotion_name' in d:
            o.promotion_name = d['promotion_name']
        return o


