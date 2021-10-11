#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class PayRcvSettleOrderDTO(object):

    def __init__(self):
        self._amount = None
        self._ant_pd_code = None
        self._apply_id = None
        self._arrangement_no = None
        self._biz_pd_code = None
        self._fund_settle_time = None
        self._initiative_settle = None
        self._inst_id = None
        self._ip_role_id = None
        self._ip_role_id_source = None
        self._memo = None
        self._order_no = None
        self._pay_date = None
        self._payee_account_branch_name = None
        self._payee_account_name = None
        self._payee_account_no = None
        self._payee_account_type = None
        self._payee_account_type_name = None
        self._payee_ip_role_id = None
        self._payer_account_branch_name = None
        self._payer_account_name = None
        self._payer_account_no = None
        self._payer_account_type = None
        self._payer_account_type_name = None
        self._payer_ip_role_id = None
        self._sales_product_code = None
        self._settle_biz_type = None
        self._settled_amount = None
        self._status = None
        self._status_name = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._amount = value
        else:
            self._amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def ant_pd_code(self):
        return self._ant_pd_code

    @ant_pd_code.setter
    def ant_pd_code(self, value):
        self._ant_pd_code = value
    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def biz_pd_code(self):
        return self._biz_pd_code

    @biz_pd_code.setter
    def biz_pd_code(self, value):
        self._biz_pd_code = value
    @property
    def fund_settle_time(self):
        return self._fund_settle_time

    @fund_settle_time.setter
    def fund_settle_time(self, value):
        self._fund_settle_time = value
    @property
    def initiative_settle(self):
        return self._initiative_settle

    @initiative_settle.setter
    def initiative_settle(self, value):
        self._initiative_settle = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def ip_role_id_source(self):
        return self._ip_role_id_source

    @ip_role_id_source.setter
    def ip_role_id_source(self, value):
        self._ip_role_id_source = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def payee_account_branch_name(self):
        return self._payee_account_branch_name

    @payee_account_branch_name.setter
    def payee_account_branch_name(self, value):
        self._payee_account_branch_name = value
    @property
    def payee_account_name(self):
        return self._payee_account_name

    @payee_account_name.setter
    def payee_account_name(self, value):
        self._payee_account_name = value
    @property
    def payee_account_no(self):
        return self._payee_account_no

    @payee_account_no.setter
    def payee_account_no(self, value):
        self._payee_account_no = value
    @property
    def payee_account_type(self):
        return self._payee_account_type

    @payee_account_type.setter
    def payee_account_type(self, value):
        self._payee_account_type = value
    @property
    def payee_account_type_name(self):
        return self._payee_account_type_name

    @payee_account_type_name.setter
    def payee_account_type_name(self, value):
        self._payee_account_type_name = value
    @property
    def payee_ip_role_id(self):
        return self._payee_ip_role_id

    @payee_ip_role_id.setter
    def payee_ip_role_id(self, value):
        self._payee_ip_role_id = value
    @property
    def payer_account_branch_name(self):
        return self._payer_account_branch_name

    @payer_account_branch_name.setter
    def payer_account_branch_name(self, value):
        self._payer_account_branch_name = value
    @property
    def payer_account_name(self):
        return self._payer_account_name

    @payer_account_name.setter
    def payer_account_name(self, value):
        self._payer_account_name = value
    @property
    def payer_account_no(self):
        return self._payer_account_no

    @payer_account_no.setter
    def payer_account_no(self, value):
        self._payer_account_no = value
    @property
    def payer_account_type(self):
        return self._payer_account_type

    @payer_account_type.setter
    def payer_account_type(self, value):
        self._payer_account_type = value
    @property
    def payer_account_type_name(self):
        return self._payer_account_type_name

    @payer_account_type_name.setter
    def payer_account_type_name(self, value):
        self._payer_account_type_name = value
    @property
    def payer_ip_role_id(self):
        return self._payer_ip_role_id

    @payer_ip_role_id.setter
    def payer_ip_role_id(self, value):
        self._payer_ip_role_id = value
    @property
    def sales_product_code(self):
        return self._sales_product_code

    @sales_product_code.setter
    def sales_product_code(self, value):
        self._sales_product_code = value
    @property
    def settle_biz_type(self):
        return self._settle_biz_type

    @settle_biz_type.setter
    def settle_biz_type(self, value):
        self._settle_biz_type = value
    @property
    def settled_amount(self):
        return self._settled_amount

    @settled_amount.setter
    def settled_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._settled_amount = value
        else:
            self._settled_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_name(self):
        return self._status_name

    @status_name.setter
    def status_name(self, value):
        self._status_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.ant_pd_code:
            if hasattr(self.ant_pd_code, 'to_alipay_dict'):
                params['ant_pd_code'] = self.ant_pd_code.to_alipay_dict()
            else:
                params['ant_pd_code'] = self.ant_pd_code
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.biz_pd_code:
            if hasattr(self.biz_pd_code, 'to_alipay_dict'):
                params['biz_pd_code'] = self.biz_pd_code.to_alipay_dict()
            else:
                params['biz_pd_code'] = self.biz_pd_code
        if self.fund_settle_time:
            if hasattr(self.fund_settle_time, 'to_alipay_dict'):
                params['fund_settle_time'] = self.fund_settle_time.to_alipay_dict()
            else:
                params['fund_settle_time'] = self.fund_settle_time
        if self.initiative_settle:
            if hasattr(self.initiative_settle, 'to_alipay_dict'):
                params['initiative_settle'] = self.initiative_settle.to_alipay_dict()
            else:
                params['initiative_settle'] = self.initiative_settle
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.ip_role_id_source:
            if hasattr(self.ip_role_id_source, 'to_alipay_dict'):
                params['ip_role_id_source'] = self.ip_role_id_source.to_alipay_dict()
            else:
                params['ip_role_id_source'] = self.ip_role_id_source
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.payee_account_branch_name:
            if hasattr(self.payee_account_branch_name, 'to_alipay_dict'):
                params['payee_account_branch_name'] = self.payee_account_branch_name.to_alipay_dict()
            else:
                params['payee_account_branch_name'] = self.payee_account_branch_name
        if self.payee_account_name:
            if hasattr(self.payee_account_name, 'to_alipay_dict'):
                params['payee_account_name'] = self.payee_account_name.to_alipay_dict()
            else:
                params['payee_account_name'] = self.payee_account_name
        if self.payee_account_no:
            if hasattr(self.payee_account_no, 'to_alipay_dict'):
                params['payee_account_no'] = self.payee_account_no.to_alipay_dict()
            else:
                params['payee_account_no'] = self.payee_account_no
        if self.payee_account_type:
            if hasattr(self.payee_account_type, 'to_alipay_dict'):
                params['payee_account_type'] = self.payee_account_type.to_alipay_dict()
            else:
                params['payee_account_type'] = self.payee_account_type
        if self.payee_account_type_name:
            if hasattr(self.payee_account_type_name, 'to_alipay_dict'):
                params['payee_account_type_name'] = self.payee_account_type_name.to_alipay_dict()
            else:
                params['payee_account_type_name'] = self.payee_account_type_name
        if self.payee_ip_role_id:
            if hasattr(self.payee_ip_role_id, 'to_alipay_dict'):
                params['payee_ip_role_id'] = self.payee_ip_role_id.to_alipay_dict()
            else:
                params['payee_ip_role_id'] = self.payee_ip_role_id
        if self.payer_account_branch_name:
            if hasattr(self.payer_account_branch_name, 'to_alipay_dict'):
                params['payer_account_branch_name'] = self.payer_account_branch_name.to_alipay_dict()
            else:
                params['payer_account_branch_name'] = self.payer_account_branch_name
        if self.payer_account_name:
            if hasattr(self.payer_account_name, 'to_alipay_dict'):
                params['payer_account_name'] = self.payer_account_name.to_alipay_dict()
            else:
                params['payer_account_name'] = self.payer_account_name
        if self.payer_account_no:
            if hasattr(self.payer_account_no, 'to_alipay_dict'):
                params['payer_account_no'] = self.payer_account_no.to_alipay_dict()
            else:
                params['payer_account_no'] = self.payer_account_no
        if self.payer_account_type:
            if hasattr(self.payer_account_type, 'to_alipay_dict'):
                params['payer_account_type'] = self.payer_account_type.to_alipay_dict()
            else:
                params['payer_account_type'] = self.payer_account_type
        if self.payer_account_type_name:
            if hasattr(self.payer_account_type_name, 'to_alipay_dict'):
                params['payer_account_type_name'] = self.payer_account_type_name.to_alipay_dict()
            else:
                params['payer_account_type_name'] = self.payer_account_type_name
        if self.payer_ip_role_id:
            if hasattr(self.payer_ip_role_id, 'to_alipay_dict'):
                params['payer_ip_role_id'] = self.payer_ip_role_id.to_alipay_dict()
            else:
                params['payer_ip_role_id'] = self.payer_ip_role_id
        if self.sales_product_code:
            if hasattr(self.sales_product_code, 'to_alipay_dict'):
                params['sales_product_code'] = self.sales_product_code.to_alipay_dict()
            else:
                params['sales_product_code'] = self.sales_product_code
        if self.settle_biz_type:
            if hasattr(self.settle_biz_type, 'to_alipay_dict'):
                params['settle_biz_type'] = self.settle_biz_type.to_alipay_dict()
            else:
                params['settle_biz_type'] = self.settle_biz_type
        if self.settled_amount:
            if hasattr(self.settled_amount, 'to_alipay_dict'):
                params['settled_amount'] = self.settled_amount.to_alipay_dict()
            else:
                params['settled_amount'] = self.settled_amount
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_name:
            if hasattr(self.status_name, 'to_alipay_dict'):
                params['status_name'] = self.status_name.to_alipay_dict()
            else:
                params['status_name'] = self.status_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayRcvSettleOrderDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'ant_pd_code' in d:
            o.ant_pd_code = d['ant_pd_code']
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'biz_pd_code' in d:
            o.biz_pd_code = d['biz_pd_code']
        if 'fund_settle_time' in d:
            o.fund_settle_time = d['fund_settle_time']
        if 'initiative_settle' in d:
            o.initiative_settle = d['initiative_settle']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'ip_role_id_source' in d:
            o.ip_role_id_source = d['ip_role_id_source']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'payee_account_branch_name' in d:
            o.payee_account_branch_name = d['payee_account_branch_name']
        if 'payee_account_name' in d:
            o.payee_account_name = d['payee_account_name']
        if 'payee_account_no' in d:
            o.payee_account_no = d['payee_account_no']
        if 'payee_account_type' in d:
            o.payee_account_type = d['payee_account_type']
        if 'payee_account_type_name' in d:
            o.payee_account_type_name = d['payee_account_type_name']
        if 'payee_ip_role_id' in d:
            o.payee_ip_role_id = d['payee_ip_role_id']
        if 'payer_account_branch_name' in d:
            o.payer_account_branch_name = d['payer_account_branch_name']
        if 'payer_account_name' in d:
            o.payer_account_name = d['payer_account_name']
        if 'payer_account_no' in d:
            o.payer_account_no = d['payer_account_no']
        if 'payer_account_type' in d:
            o.payer_account_type = d['payer_account_type']
        if 'payer_account_type_name' in d:
            o.payer_account_type_name = d['payer_account_type_name']
        if 'payer_ip_role_id' in d:
            o.payer_ip_role_id = d['payer_ip_role_id']
        if 'sales_product_code' in d:
            o.sales_product_code = d['sales_product_code']
        if 'settle_biz_type' in d:
            o.settle_biz_type = d['settle_biz_type']
        if 'settled_amount' in d:
            o.settled_amount = d['settled_amount']
        if 'status' in d:
            o.status = d['status']
        if 'status_name' in d:
            o.status_name = d['status_name']
        return o


