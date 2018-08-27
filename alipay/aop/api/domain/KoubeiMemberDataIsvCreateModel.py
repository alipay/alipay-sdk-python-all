#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MemberShip import MemberShip
from alipay.aop.api.domain.OuterMemberInfo import OuterMemberInfo


class KoubeiMemberDataIsvCreateModel(object):

    def __init__(self):
        self._gmt_member_card_last_active = None
        self._gmt_merber_card_create = None
        self._member_card_id = None
        self._member_card_type = None
        self._member_ship = None
        self._member_source = None
        self._member_source_desc = None
        self._member_status = None
        self._outer_member_info = None
        self._parter_id = None
        self._shop_id = None

    @property
    def gmt_member_card_last_active(self):
        return self._gmt_member_card_last_active

    @gmt_member_card_last_active.setter
    def gmt_member_card_last_active(self, value):
        self._gmt_member_card_last_active = value
    @property
    def gmt_merber_card_create(self):
        return self._gmt_merber_card_create

    @gmt_merber_card_create.setter
    def gmt_merber_card_create(self, value):
        self._gmt_merber_card_create = value
    @property
    def member_card_id(self):
        return self._member_card_id

    @member_card_id.setter
    def member_card_id(self, value):
        self._member_card_id = value
    @property
    def member_card_type(self):
        return self._member_card_type

    @member_card_type.setter
    def member_card_type(self, value):
        self._member_card_type = value
    @property
    def member_ship(self):
        return self._member_ship

    @member_ship.setter
    def member_ship(self, value):
        if isinstance(value, MemberShip):
            self._member_ship = value
        else:
            self._member_ship = MemberShip.from_alipay_dict(value)
    @property
    def member_source(self):
        return self._member_source

    @member_source.setter
    def member_source(self, value):
        self._member_source = value
    @property
    def member_source_desc(self):
        return self._member_source_desc

    @member_source_desc.setter
    def member_source_desc(self, value):
        self._member_source_desc = value
    @property
    def member_status(self):
        return self._member_status

    @member_status.setter
    def member_status(self, value):
        self._member_status = value
    @property
    def outer_member_info(self):
        return self._outer_member_info

    @outer_member_info.setter
    def outer_member_info(self, value):
        if isinstance(value, OuterMemberInfo):
            self._outer_member_info = value
        else:
            self._outer_member_info = OuterMemberInfo.from_alipay_dict(value)
    @property
    def parter_id(self):
        return self._parter_id

    @parter_id.setter
    def parter_id(self, value):
        self._parter_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_member_card_last_active:
            if hasattr(self.gmt_member_card_last_active, 'to_alipay_dict'):
                params['gmt_member_card_last_active'] = self.gmt_member_card_last_active.to_alipay_dict()
            else:
                params['gmt_member_card_last_active'] = self.gmt_member_card_last_active
        if self.gmt_merber_card_create:
            if hasattr(self.gmt_merber_card_create, 'to_alipay_dict'):
                params['gmt_merber_card_create'] = self.gmt_merber_card_create.to_alipay_dict()
            else:
                params['gmt_merber_card_create'] = self.gmt_merber_card_create
        if self.member_card_id:
            if hasattr(self.member_card_id, 'to_alipay_dict'):
                params['member_card_id'] = self.member_card_id.to_alipay_dict()
            else:
                params['member_card_id'] = self.member_card_id
        if self.member_card_type:
            if hasattr(self.member_card_type, 'to_alipay_dict'):
                params['member_card_type'] = self.member_card_type.to_alipay_dict()
            else:
                params['member_card_type'] = self.member_card_type
        if self.member_ship:
            if hasattr(self.member_ship, 'to_alipay_dict'):
                params['member_ship'] = self.member_ship.to_alipay_dict()
            else:
                params['member_ship'] = self.member_ship
        if self.member_source:
            if hasattr(self.member_source, 'to_alipay_dict'):
                params['member_source'] = self.member_source.to_alipay_dict()
            else:
                params['member_source'] = self.member_source
        if self.member_source_desc:
            if hasattr(self.member_source_desc, 'to_alipay_dict'):
                params['member_source_desc'] = self.member_source_desc.to_alipay_dict()
            else:
                params['member_source_desc'] = self.member_source_desc
        if self.member_status:
            if hasattr(self.member_status, 'to_alipay_dict'):
                params['member_status'] = self.member_status.to_alipay_dict()
            else:
                params['member_status'] = self.member_status
        if self.outer_member_info:
            if hasattr(self.outer_member_info, 'to_alipay_dict'):
                params['outer_member_info'] = self.outer_member_info.to_alipay_dict()
            else:
                params['outer_member_info'] = self.outer_member_info
        if self.parter_id:
            if hasattr(self.parter_id, 'to_alipay_dict'):
                params['parter_id'] = self.parter_id.to_alipay_dict()
            else:
                params['parter_id'] = self.parter_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMemberDataIsvCreateModel()
        if 'gmt_member_card_last_active' in d:
            o.gmt_member_card_last_active = d['gmt_member_card_last_active']
        if 'gmt_merber_card_create' in d:
            o.gmt_merber_card_create = d['gmt_merber_card_create']
        if 'member_card_id' in d:
            o.member_card_id = d['member_card_id']
        if 'member_card_type' in d:
            o.member_card_type = d['member_card_type']
        if 'member_ship' in d:
            o.member_ship = d['member_ship']
        if 'member_source' in d:
            o.member_source = d['member_source']
        if 'member_source_desc' in d:
            o.member_source_desc = d['member_source_desc']
        if 'member_status' in d:
            o.member_status = d['member_status']
        if 'outer_member_info' in d:
            o.outer_member_info = d['outer_member_info']
        if 'parter_id' in d:
            o.parter_id = d['parter_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


