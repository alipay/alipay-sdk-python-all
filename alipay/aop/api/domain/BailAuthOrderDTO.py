#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BailAuthOrderDTO(object):

    def __init__(self):
        self._agreement_no = None
        self._amount = None
        self._auth_no = None
        self._bail_status = None
        self._fund_entrust_type = None
        self._gmt_create = None
        self._gmt_modified = None
        self._order_title = None
        self._partner_user_id = None
        self._product_code = None
        self._scene_code = None
        self._scene_desc = None
        self._user_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def bail_status(self):
        return self._bail_status

    @bail_status.setter
    def bail_status(self, value):
        self._bail_status = value
    @property
    def fund_entrust_type(self):
        return self._fund_entrust_type

    @fund_entrust_type.setter
    def fund_entrust_type(self, value):
        self._fund_entrust_type = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def partner_user_id(self):
        return self._partner_user_id

    @partner_user_id.setter
    def partner_user_id(self, value):
        self._partner_user_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_desc(self):
        return self._scene_desc

    @scene_desc.setter
    def scene_desc(self, value):
        self._scene_desc = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.auth_no:
            if hasattr(self.auth_no, 'to_alipay_dict'):
                params['auth_no'] = self.auth_no.to_alipay_dict()
            else:
                params['auth_no'] = self.auth_no
        if self.bail_status:
            if hasattr(self.bail_status, 'to_alipay_dict'):
                params['bail_status'] = self.bail_status.to_alipay_dict()
            else:
                params['bail_status'] = self.bail_status
        if self.fund_entrust_type:
            if hasattr(self.fund_entrust_type, 'to_alipay_dict'):
                params['fund_entrust_type'] = self.fund_entrust_type.to_alipay_dict()
            else:
                params['fund_entrust_type'] = self.fund_entrust_type
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.partner_user_id:
            if hasattr(self.partner_user_id, 'to_alipay_dict'):
                params['partner_user_id'] = self.partner_user_id.to_alipay_dict()
            else:
                params['partner_user_id'] = self.partner_user_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_desc:
            if hasattr(self.scene_desc, 'to_alipay_dict'):
                params['scene_desc'] = self.scene_desc.to_alipay_dict()
            else:
                params['scene_desc'] = self.scene_desc
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BailAuthOrderDTO()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'auth_no' in d:
            o.auth_no = d['auth_no']
        if 'bail_status' in d:
            o.bail_status = d['bail_status']
        if 'fund_entrust_type' in d:
            o.fund_entrust_type = d['fund_entrust_type']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'partner_user_id' in d:
            o.partner_user_id = d['partner_user_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_desc' in d:
            o.scene_desc = d['scene_desc']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


