#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoLogisticsExpressOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoLogisticsExpressOrderQueryResponse, self).__init__()
        self._accept_type = None
        self._cancel_cause = None
        self._courier_alipay_account = None
        self._courier_emp_num = None
        self._courier_id_card = None
        self._courier_mobile = None
        self._courier_name = None
        self._create_time = None
        self._fare_claims_amount = None
        self._last_modified_time = None
        self._logis_merch_code = None
        self._order_amount = None
        self._order_no = None
        self._order_status = None
        self._pay_status = None
        self._product_type_change_reason = None
        self._product_type_code = None
        self._site_area_code = None
        self._site_code = None
        self._site_complain_tel = None
        self._site_detail_addr = None
        self._site_leader_mobile = None
        self._site_leader_name = None
        self._site_name = None
        self._trade_amount = None
        self._trade_no = None
        self._way_bill_no = None

    @property
    def accept_type(self):
        return self._accept_type

    @accept_type.setter
    def accept_type(self, value):
        self._accept_type = value
    @property
    def cancel_cause(self):
        return self._cancel_cause

    @cancel_cause.setter
    def cancel_cause(self, value):
        self._cancel_cause = value
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
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def fare_claims_amount(self):
        return self._fare_claims_amount

    @fare_claims_amount.setter
    def fare_claims_amount(self, value):
        self._fare_claims_amount = value
    @property
    def last_modified_time(self):
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, value):
        self._last_modified_time = value
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
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
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
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def way_bill_no(self):
        return self._way_bill_no

    @way_bill_no.setter
    def way_bill_no(self, value):
        self._way_bill_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoLogisticsExpressOrderQueryResponse, self).parse_response_content(response_content)
        if 'accept_type' in response:
            self.accept_type = response['accept_type']
        if 'cancel_cause' in response:
            self.cancel_cause = response['cancel_cause']
        if 'courier_alipay_account' in response:
            self.courier_alipay_account = response['courier_alipay_account']
        if 'courier_emp_num' in response:
            self.courier_emp_num = response['courier_emp_num']
        if 'courier_id_card' in response:
            self.courier_id_card = response['courier_id_card']
        if 'courier_mobile' in response:
            self.courier_mobile = response['courier_mobile']
        if 'courier_name' in response:
            self.courier_name = response['courier_name']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'fare_claims_amount' in response:
            self.fare_claims_amount = response['fare_claims_amount']
        if 'last_modified_time' in response:
            self.last_modified_time = response['last_modified_time']
        if 'logis_merch_code' in response:
            self.logis_merch_code = response['logis_merch_code']
        if 'order_amount' in response:
            self.order_amount = response['order_amount']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'pay_status' in response:
            self.pay_status = response['pay_status']
        if 'product_type_change_reason' in response:
            self.product_type_change_reason = response['product_type_change_reason']
        if 'product_type_code' in response:
            self.product_type_code = response['product_type_code']
        if 'site_area_code' in response:
            self.site_area_code = response['site_area_code']
        if 'site_code' in response:
            self.site_code = response['site_code']
        if 'site_complain_tel' in response:
            self.site_complain_tel = response['site_complain_tel']
        if 'site_detail_addr' in response:
            self.site_detail_addr = response['site_detail_addr']
        if 'site_leader_mobile' in response:
            self.site_leader_mobile = response['site_leader_mobile']
        if 'site_leader_name' in response:
            self.site_leader_name = response['site_leader_name']
        if 'site_name' in response:
            self.site_name = response['site_name']
        if 'trade_amount' in response:
            self.trade_amount = response['trade_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'way_bill_no' in response:
            self.way_bill_no = response['way_bill_no']
