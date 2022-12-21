#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenFundComponentDetailDTO import OpenFundComponentDetailDTO
from alipay.aop.api.domain.OpenFundInfo import OpenFundInfo


class OpenVoucherTradeFundDetail(object):

    def __init__(self):
        self._amount = None
        self._assets_code = None
        self._biz_context = None
        self._biz_ev_code = None
        self._biz_pd_code = None
        self._biz_type = None
        self._cash = None
        self._cnl_ev_code = None
        self._cnl_no = None
        self._cnl_pd_code = None
        self._detail_id = None
        self._detail_tag = None
        self._ev_code = None
        self._extend_info = None
        self._fund_component_detail_list = None
        self._fund_infos = None
        self._gmt_create = None
        self._gmt_modified = None
        self._item_ids = None
        self._name = None
        self._order_id = None
        self._pd_code = None
        self._product_code = None
        self._status = None
        self._template_id = None
        self._trade_no = None
        self._user_id = None
        self._voucher_description = None
        self._voucher_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def assets_code(self):
        return self._assets_code

    @assets_code.setter
    def assets_code(self, value):
        self._assets_code = value
    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        self._biz_context = value
    @property
    def biz_ev_code(self):
        return self._biz_ev_code

    @biz_ev_code.setter
    def biz_ev_code(self, value):
        self._biz_ev_code = value
    @property
    def biz_pd_code(self):
        return self._biz_pd_code

    @biz_pd_code.setter
    def biz_pd_code(self, value):
        self._biz_pd_code = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        self._cash = value
    @property
    def cnl_ev_code(self):
        return self._cnl_ev_code

    @cnl_ev_code.setter
    def cnl_ev_code(self, value):
        self._cnl_ev_code = value
    @property
    def cnl_no(self):
        return self._cnl_no

    @cnl_no.setter
    def cnl_no(self, value):
        self._cnl_no = value
    @property
    def cnl_pd_code(self):
        return self._cnl_pd_code

    @cnl_pd_code.setter
    def cnl_pd_code(self, value):
        self._cnl_pd_code = value
    @property
    def detail_id(self):
        return self._detail_id

    @detail_id.setter
    def detail_id(self, value):
        self._detail_id = value
    @property
    def detail_tag(self):
        return self._detail_tag

    @detail_tag.setter
    def detail_tag(self, value):
        self._detail_tag = value
    @property
    def ev_code(self):
        return self._ev_code

    @ev_code.setter
    def ev_code(self, value):
        self._ev_code = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def fund_component_detail_list(self):
        return self._fund_component_detail_list

    @fund_component_detail_list.setter
    def fund_component_detail_list(self, value):
        if isinstance(value, list):
            self._fund_component_detail_list = list()
            for i in value:
                if isinstance(i, OpenFundComponentDetailDTO):
                    self._fund_component_detail_list.append(i)
                else:
                    self._fund_component_detail_list.append(OpenFundComponentDetailDTO.from_alipay_dict(i))
    @property
    def fund_infos(self):
        return self._fund_infos

    @fund_infos.setter
    def fund_infos(self, value):
        if isinstance(value, list):
            self._fund_infos = list()
            for i in value:
                if isinstance(i, OpenFundInfo):
                    self._fund_infos.append(i)
                else:
                    self._fund_infos.append(OpenFundInfo.from_alipay_dict(i))
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
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        if isinstance(value, list):
            self._item_ids = list()
            for i in value:
                self._item_ids.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def pd_code(self):
        return self._pd_code

    @pd_code.setter
    def pd_code(self, value):
        self._pd_code = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voucher_description(self):
        return self._voucher_description

    @voucher_description.setter
    def voucher_description(self, value):
        self._voucher_description = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.assets_code:
            if hasattr(self.assets_code, 'to_alipay_dict'):
                params['assets_code'] = self.assets_code.to_alipay_dict()
            else:
                params['assets_code'] = self.assets_code
        if self.biz_context:
            if hasattr(self.biz_context, 'to_alipay_dict'):
                params['biz_context'] = self.biz_context.to_alipay_dict()
            else:
                params['biz_context'] = self.biz_context
        if self.biz_ev_code:
            if hasattr(self.biz_ev_code, 'to_alipay_dict'):
                params['biz_ev_code'] = self.biz_ev_code.to_alipay_dict()
            else:
                params['biz_ev_code'] = self.biz_ev_code
        if self.biz_pd_code:
            if hasattr(self.biz_pd_code, 'to_alipay_dict'):
                params['biz_pd_code'] = self.biz_pd_code.to_alipay_dict()
            else:
                params['biz_pd_code'] = self.biz_pd_code
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cash:
            if hasattr(self.cash, 'to_alipay_dict'):
                params['cash'] = self.cash.to_alipay_dict()
            else:
                params['cash'] = self.cash
        if self.cnl_ev_code:
            if hasattr(self.cnl_ev_code, 'to_alipay_dict'):
                params['cnl_ev_code'] = self.cnl_ev_code.to_alipay_dict()
            else:
                params['cnl_ev_code'] = self.cnl_ev_code
        if self.cnl_no:
            if hasattr(self.cnl_no, 'to_alipay_dict'):
                params['cnl_no'] = self.cnl_no.to_alipay_dict()
            else:
                params['cnl_no'] = self.cnl_no
        if self.cnl_pd_code:
            if hasattr(self.cnl_pd_code, 'to_alipay_dict'):
                params['cnl_pd_code'] = self.cnl_pd_code.to_alipay_dict()
            else:
                params['cnl_pd_code'] = self.cnl_pd_code
        if self.detail_id:
            if hasattr(self.detail_id, 'to_alipay_dict'):
                params['detail_id'] = self.detail_id.to_alipay_dict()
            else:
                params['detail_id'] = self.detail_id
        if self.detail_tag:
            if hasattr(self.detail_tag, 'to_alipay_dict'):
                params['detail_tag'] = self.detail_tag.to_alipay_dict()
            else:
                params['detail_tag'] = self.detail_tag
        if self.ev_code:
            if hasattr(self.ev_code, 'to_alipay_dict'):
                params['ev_code'] = self.ev_code.to_alipay_dict()
            else:
                params['ev_code'] = self.ev_code
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.fund_component_detail_list:
            if isinstance(self.fund_component_detail_list, list):
                for i in range(0, len(self.fund_component_detail_list)):
                    element = self.fund_component_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_component_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.fund_component_detail_list, 'to_alipay_dict'):
                params['fund_component_detail_list'] = self.fund_component_detail_list.to_alipay_dict()
            else:
                params['fund_component_detail_list'] = self.fund_component_detail_list
        if self.fund_infos:
            if isinstance(self.fund_infos, list):
                for i in range(0, len(self.fund_infos)):
                    element = self.fund_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_infos[i] = element.to_alipay_dict()
            if hasattr(self.fund_infos, 'to_alipay_dict'):
                params['fund_infos'] = self.fund_infos.to_alipay_dict()
            else:
                params['fund_infos'] = self.fund_infos
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
        if self.item_ids:
            if isinstance(self.item_ids, list):
                for i in range(0, len(self.item_ids)):
                    element = self.item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_ids[i] = element.to_alipay_dict()
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.pd_code:
            if hasattr(self.pd_code, 'to_alipay_dict'):
                params['pd_code'] = self.pd_code.to_alipay_dict()
            else:
                params['pd_code'] = self.pd_code
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.voucher_description:
            if hasattr(self.voucher_description, 'to_alipay_dict'):
                params['voucher_description'] = self.voucher_description.to_alipay_dict()
            else:
                params['voucher_description'] = self.voucher_description
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenVoucherTradeFundDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'assets_code' in d:
            o.assets_code = d['assets_code']
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'biz_ev_code' in d:
            o.biz_ev_code = d['biz_ev_code']
        if 'biz_pd_code' in d:
            o.biz_pd_code = d['biz_pd_code']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cash' in d:
            o.cash = d['cash']
        if 'cnl_ev_code' in d:
            o.cnl_ev_code = d['cnl_ev_code']
        if 'cnl_no' in d:
            o.cnl_no = d['cnl_no']
        if 'cnl_pd_code' in d:
            o.cnl_pd_code = d['cnl_pd_code']
        if 'detail_id' in d:
            o.detail_id = d['detail_id']
        if 'detail_tag' in d:
            o.detail_tag = d['detail_tag']
        if 'ev_code' in d:
            o.ev_code = d['ev_code']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'fund_component_detail_list' in d:
            o.fund_component_detail_list = d['fund_component_detail_list']
        if 'fund_infos' in d:
            o.fund_infos = d['fund_infos']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        if 'name' in d:
            o.name = d['name']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'pd_code' in d:
            o.pd_code = d['pd_code']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'status' in d:
            o.status = d['status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'voucher_description' in d:
            o.voucher_description = d['voucher_description']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


