#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoLogisticsExpressOrderModifyModel(object):

    def __init__(self):
        self._accept_type = None
        self._courier_alipay_account = None
        self._courier_emp_num = None
        self._courier_head_img = None
        self._courier_id_card = None
        self._courier_mobile = None
        self._courier_name = None
        self._goods_weight = None
        self._logis_merch_code = None
        self._order_amount = None
        self._order_no = None
        self._order_status = None
        self._product_type_change_reason = None
        self._product_type_code = None
        self._refuse_code = None
        self._refuse_desc = None
        self._site_area_code = None
        self._site_code = None
        self._site_complain_tel = None
        self._site_detail_addr = None
        self._site_leader_mobile = None
        self._site_leader_name = None
        self._site_name = None
        self._way_bill_no = None

    @property
    def accept_type(self):
        return self._accept_type

    @accept_type.setter
    def accept_type(self, value):
        self._accept_type = value
    @property
    def courier_alipay_account(self):
        return self._courier_alipay_account

    @courier_alipay_account.setter
    def courier_alipay_account(self, value):
        self._courier_alipay_account = value
    @property
    def courier_emp_num(self):
        return self._courier_emp_num

    @courier_emp_num.setter
    def courier_emp_num(self, value):
        self._courier_emp_num = value
    @property
    def courier_head_img(self):
        return self._courier_head_img

    @courier_head_img.setter
    def courier_head_img(self, value):
        self._courier_head_img = value
    @property
    def courier_id_card(self):
        return self._courier_id_card

    @courier_id_card.setter
    def courier_id_card(self, value):
        self._courier_id_card = value
    @property
    def courier_mobile(self):
        return self._courier_mobile

    @courier_mobile.setter
    def courier_mobile(self, value):
        self._courier_mobile = value
    @property
    def courier_name(self):
        return self._courier_name

    @courier_name.setter
    def courier_name(self, value):
        self._courier_name = value
    @property
    def goods_weight(self):
        return self._goods_weight

    @goods_weight.setter
    def goods_weight(self, value):
        self._goods_weight = value
    @property
    def logis_merch_code(self):
        return self._logis_merch_code

    @logis_merch_code.setter
    def logis_merch_code(self, value):
        self._logis_merch_code = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def product_type_change_reason(self):
        return self._product_type_change_reason

    @product_type_change_reason.setter
    def product_type_change_reason(self, value):
        self._product_type_change_reason = value
    @property
    def product_type_code(self):
        return self._product_type_code

    @product_type_code.setter
    def product_type_code(self, value):
        self._product_type_code = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_desc(self):
        return self._refuse_desc

    @refuse_desc.setter
    def refuse_desc(self, value):
        self._refuse_desc = value
    @property
    def site_area_code(self):
        return self._site_area_code

    @site_area_code.setter
    def site_area_code(self, value):
        self._site_area_code = value
    @property
    def site_code(self):
        return self._site_code

    @site_code.setter
    def site_code(self, value):
        self._site_code = value
    @property
    def site_complain_tel(self):
        return self._site_complain_tel

    @site_complain_tel.setter
    def site_complain_tel(self, value):
        self._site_complain_tel = value
    @property
    def site_detail_addr(self):
        return self._site_detail_addr

    @site_detail_addr.setter
    def site_detail_addr(self, value):
        self._site_detail_addr = value
    @property
    def site_leader_mobile(self):
        return self._site_leader_mobile

    @site_leader_mobile.setter
    def site_leader_mobile(self, value):
        self._site_leader_mobile = value
    @property
    def site_leader_name(self):
        return self._site_leader_name

    @site_leader_name.setter
    def site_leader_name(self, value):
        self._site_leader_name = value
    @property
    def site_name(self):
        return self._site_name

    @site_name.setter
    def site_name(self, value):
        self._site_name = value
    @property
    def way_bill_no(self):
        return self._way_bill_no

    @way_bill_no.setter
    def way_bill_no(self, value):
        self._way_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.accept_type:
            if hasattr(self.accept_type, 'to_alipay_dict'):
                params['accept_type'] = self.accept_type.to_alipay_dict()
            else:
                params['accept_type'] = self.accept_type
        if self.courier_alipay_account:
            if hasattr(self.courier_alipay_account, 'to_alipay_dict'):
                params['courier_alipay_account'] = self.courier_alipay_account.to_alipay_dict()
            else:
                params['courier_alipay_account'] = self.courier_alipay_account
        if self.courier_emp_num:
            if hasattr(self.courier_emp_num, 'to_alipay_dict'):
                params['courier_emp_num'] = self.courier_emp_num.to_alipay_dict()
            else:
                params['courier_emp_num'] = self.courier_emp_num
        if self.courier_head_img:
            if hasattr(self.courier_head_img, 'to_alipay_dict'):
                params['courier_head_img'] = self.courier_head_img.to_alipay_dict()
            else:
                params['courier_head_img'] = self.courier_head_img
        if self.courier_id_card:
            if hasattr(self.courier_id_card, 'to_alipay_dict'):
                params['courier_id_card'] = self.courier_id_card.to_alipay_dict()
            else:
                params['courier_id_card'] = self.courier_id_card
        if self.courier_mobile:
            if hasattr(self.courier_mobile, 'to_alipay_dict'):
                params['courier_mobile'] = self.courier_mobile.to_alipay_dict()
            else:
                params['courier_mobile'] = self.courier_mobile
        if self.courier_name:
            if hasattr(self.courier_name, 'to_alipay_dict'):
                params['courier_name'] = self.courier_name.to_alipay_dict()
            else:
                params['courier_name'] = self.courier_name
        if self.goods_weight:
            if hasattr(self.goods_weight, 'to_alipay_dict'):
                params['goods_weight'] = self.goods_weight.to_alipay_dict()
            else:
                params['goods_weight'] = self.goods_weight
        if self.logis_merch_code:
            if hasattr(self.logis_merch_code, 'to_alipay_dict'):
                params['logis_merch_code'] = self.logis_merch_code.to_alipay_dict()
            else:
                params['logis_merch_code'] = self.logis_merch_code
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.product_type_change_reason:
            if hasattr(self.product_type_change_reason, 'to_alipay_dict'):
                params['product_type_change_reason'] = self.product_type_change_reason.to_alipay_dict()
            else:
                params['product_type_change_reason'] = self.product_type_change_reason
        if self.product_type_code:
            if hasattr(self.product_type_code, 'to_alipay_dict'):
                params['product_type_code'] = self.product_type_code.to_alipay_dict()
            else:
                params['product_type_code'] = self.product_type_code
        if self.refuse_code:
            if hasattr(self.refuse_code, 'to_alipay_dict'):
                params['refuse_code'] = self.refuse_code.to_alipay_dict()
            else:
                params['refuse_code'] = self.refuse_code
        if self.refuse_desc:
            if hasattr(self.refuse_desc, 'to_alipay_dict'):
                params['refuse_desc'] = self.refuse_desc.to_alipay_dict()
            else:
                params['refuse_desc'] = self.refuse_desc
        if self.site_area_code:
            if hasattr(self.site_area_code, 'to_alipay_dict'):
                params['site_area_code'] = self.site_area_code.to_alipay_dict()
            else:
                params['site_area_code'] = self.site_area_code
        if self.site_code:
            if hasattr(self.site_code, 'to_alipay_dict'):
                params['site_code'] = self.site_code.to_alipay_dict()
            else:
                params['site_code'] = self.site_code
        if self.site_complain_tel:
            if hasattr(self.site_complain_tel, 'to_alipay_dict'):
                params['site_complain_tel'] = self.site_complain_tel.to_alipay_dict()
            else:
                params['site_complain_tel'] = self.site_complain_tel
        if self.site_detail_addr:
            if hasattr(self.site_detail_addr, 'to_alipay_dict'):
                params['site_detail_addr'] = self.site_detail_addr.to_alipay_dict()
            else:
                params['site_detail_addr'] = self.site_detail_addr
        if self.site_leader_mobile:
            if hasattr(self.site_leader_mobile, 'to_alipay_dict'):
                params['site_leader_mobile'] = self.site_leader_mobile.to_alipay_dict()
            else:
                params['site_leader_mobile'] = self.site_leader_mobile
        if self.site_leader_name:
            if hasattr(self.site_leader_name, 'to_alipay_dict'):
                params['site_leader_name'] = self.site_leader_name.to_alipay_dict()
            else:
                params['site_leader_name'] = self.site_leader_name
        if self.site_name:
            if hasattr(self.site_name, 'to_alipay_dict'):
                params['site_name'] = self.site_name.to_alipay_dict()
            else:
                params['site_name'] = self.site_name
        if self.way_bill_no:
            if hasattr(self.way_bill_no, 'to_alipay_dict'):
                params['way_bill_no'] = self.way_bill_no.to_alipay_dict()
            else:
                params['way_bill_no'] = self.way_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoLogisticsExpressOrderModifyModel()
        if 'accept_type' in d:
            o.accept_type = d['accept_type']
        if 'courier_alipay_account' in d:
            o.courier_alipay_account = d['courier_alipay_account']
        if 'courier_emp_num' in d:
            o.courier_emp_num = d['courier_emp_num']
        if 'courier_head_img' in d:
            o.courier_head_img = d['courier_head_img']
        if 'courier_id_card' in d:
            o.courier_id_card = d['courier_id_card']
        if 'courier_mobile' in d:
            o.courier_mobile = d['courier_mobile']
        if 'courier_name' in d:
            o.courier_name = d['courier_name']
        if 'goods_weight' in d:
            o.goods_weight = d['goods_weight']
        if 'logis_merch_code' in d:
            o.logis_merch_code = d['logis_merch_code']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'product_type_change_reason' in d:
            o.product_type_change_reason = d['product_type_change_reason']
        if 'product_type_code' in d:
            o.product_type_code = d['product_type_code']
        if 'refuse_code' in d:
            o.refuse_code = d['refuse_code']
        if 'refuse_desc' in d:
            o.refuse_desc = d['refuse_desc']
        if 'site_area_code' in d:
            o.site_area_code = d['site_area_code']
        if 'site_code' in d:
            o.site_code = d['site_code']
        if 'site_complain_tel' in d:
            o.site_complain_tel = d['site_complain_tel']
        if 'site_detail_addr' in d:
            o.site_detail_addr = d['site_detail_addr']
        if 'site_leader_mobile' in d:
            o.site_leader_mobile = d['site_leader_mobile']
        if 'site_leader_name' in d:
            o.site_leader_name = d['site_leader_name']
        if 'site_name' in d:
            o.site_name = d['site_name']
        if 'way_bill_no' in d:
            o.way_bill_no = d['way_bill_no']
        return o


