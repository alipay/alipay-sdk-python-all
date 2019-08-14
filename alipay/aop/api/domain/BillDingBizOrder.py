#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillDingBizOrder(object):

    def __init__(self):
        self._amount = None
        self._biz_trans_id = None
        self._biz_type = None
        self._biz_type_desc = None
        self._detail_state_desc = None
        self._detail_title = None
        self._direction = None
        self._gmt_finish = None
        self._id = None
        self._list_title = None
        self._login_id = None
        self._opp_login_id = None
        self._opp_nick_name = None
        self._opp_user_name = None
        self._order_id = None
        self._out_order_no = None
        self._sub_biz_scene = None
        self._title = None
        self._user_name = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_trans_id(self):
        return self._biz_trans_id

    @biz_trans_id.setter
    def biz_trans_id(self, value):
        self._biz_trans_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def biz_type_desc(self):
        return self._biz_type_desc

    @biz_type_desc.setter
    def biz_type_desc(self, value):
        self._biz_type_desc = value
    @property
    def detail_state_desc(self):
        return self._detail_state_desc

    @detail_state_desc.setter
    def detail_state_desc(self, value):
        self._detail_state_desc = value
    @property
    def detail_title(self):
        return self._detail_title

    @detail_title.setter
    def detail_title(self, value):
        self._detail_title = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def gmt_finish(self):
        return self._gmt_finish

    @gmt_finish.setter
    def gmt_finish(self, value):
        self._gmt_finish = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def list_title(self):
        return self._list_title

    @list_title.setter
    def list_title(self, value):
        self._list_title = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def opp_login_id(self):
        return self._opp_login_id

    @opp_login_id.setter
    def opp_login_id(self, value):
        self._opp_login_id = value
    @property
    def opp_nick_name(self):
        return self._opp_nick_name

    @opp_nick_name.setter
    def opp_nick_name(self, value):
        self._opp_nick_name = value
    @property
    def opp_user_name(self):
        return self._opp_user_name

    @opp_user_name.setter
    def opp_user_name(self, value):
        self._opp_user_name = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_trans_id:
            if hasattr(self.biz_trans_id, 'to_alipay_dict'):
                params['biz_trans_id'] = self.biz_trans_id.to_alipay_dict()
            else:
                params['biz_trans_id'] = self.biz_trans_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.biz_type_desc:
            if hasattr(self.biz_type_desc, 'to_alipay_dict'):
                params['biz_type_desc'] = self.biz_type_desc.to_alipay_dict()
            else:
                params['biz_type_desc'] = self.biz_type_desc
        if self.detail_state_desc:
            if hasattr(self.detail_state_desc, 'to_alipay_dict'):
                params['detail_state_desc'] = self.detail_state_desc.to_alipay_dict()
            else:
                params['detail_state_desc'] = self.detail_state_desc
        if self.detail_title:
            if hasattr(self.detail_title, 'to_alipay_dict'):
                params['detail_title'] = self.detail_title.to_alipay_dict()
            else:
                params['detail_title'] = self.detail_title
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.gmt_finish:
            if hasattr(self.gmt_finish, 'to_alipay_dict'):
                params['gmt_finish'] = self.gmt_finish.to_alipay_dict()
            else:
                params['gmt_finish'] = self.gmt_finish
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.list_title:
            if hasattr(self.list_title, 'to_alipay_dict'):
                params['list_title'] = self.list_title.to_alipay_dict()
            else:
                params['list_title'] = self.list_title
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.opp_login_id:
            if hasattr(self.opp_login_id, 'to_alipay_dict'):
                params['opp_login_id'] = self.opp_login_id.to_alipay_dict()
            else:
                params['opp_login_id'] = self.opp_login_id
        if self.opp_nick_name:
            if hasattr(self.opp_nick_name, 'to_alipay_dict'):
                params['opp_nick_name'] = self.opp_nick_name.to_alipay_dict()
            else:
                params['opp_nick_name'] = self.opp_nick_name
        if self.opp_user_name:
            if hasattr(self.opp_user_name, 'to_alipay_dict'):
                params['opp_user_name'] = self.opp_user_name.to_alipay_dict()
            else:
                params['opp_user_name'] = self.opp_user_name
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillDingBizOrder()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_trans_id' in d:
            o.biz_trans_id = d['biz_trans_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'biz_type_desc' in d:
            o.biz_type_desc = d['biz_type_desc']
        if 'detail_state_desc' in d:
            o.detail_state_desc = d['detail_state_desc']
        if 'detail_title' in d:
            o.detail_title = d['detail_title']
        if 'direction' in d:
            o.direction = d['direction']
        if 'gmt_finish' in d:
            o.gmt_finish = d['gmt_finish']
        if 'id' in d:
            o.id = d['id']
        if 'list_title' in d:
            o.list_title = d['list_title']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'opp_login_id' in d:
            o.opp_login_id = d['opp_login_id']
        if 'opp_nick_name' in d:
            o.opp_nick_name = d['opp_nick_name']
        if 'opp_user_name' in d:
            o.opp_user_name = d['opp_user_name']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        if 'title' in d:
            o.title = d['title']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


