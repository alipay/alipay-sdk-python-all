#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationDistributionFloworderCreateModel(object):

    def __init__(self):
        self._access_channel = None
        self._advertorial_img = None
        self._alipay_user_id = None
        self._client_ip = None
        self._encrypted_mobile = None
        self._first_channel = None
        self._fixed_position_code = None
        self._inst_order_id = None
        self._item_id = None
        self._mobile = None
        self._open_id = None
        self._package_name = None
        self._package_route = None
        self._page_id = None
        self._pay_type = None
        self._price = None
        self._protocol_sequence_id = None
        self._proxy_order_url = None
        self._report_materials_no = None
        self._sales_img = None
        self._sdk_voucher = None
        self._second_channel = None
        self._sms_code = None
        self._target_account = None
        self._user_agent = None
        self._verify_again_img = None

    @property
    def access_channel(self):
        return self._access_channel

    @access_channel.setter
    def access_channel(self, value):
        self._access_channel = value
    @property
    def advertorial_img(self):
        return self._advertorial_img

    @advertorial_img.setter
    def advertorial_img(self, value):
        self._advertorial_img = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def encrypted_mobile(self):
        return self._encrypted_mobile

    @encrypted_mobile.setter
    def encrypted_mobile(self, value):
        self._encrypted_mobile = value
    @property
    def first_channel(self):
        return self._first_channel

    @first_channel.setter
    def first_channel(self, value):
        self._first_channel = value
    @property
    def fixed_position_code(self):
        return self._fixed_position_code

    @fixed_position_code.setter
    def fixed_position_code(self, value):
        self._fixed_position_code = value
    @property
    def inst_order_id(self):
        return self._inst_order_id

    @inst_order_id.setter
    def inst_order_id(self, value):
        self._inst_order_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def package_name(self):
        return self._package_name

    @package_name.setter
    def package_name(self, value):
        self._package_name = value
    @property
    def package_route(self):
        return self._package_route

    @package_route.setter
    def package_route(self, value):
        self._package_route = value
    @property
    def page_id(self):
        return self._page_id

    @page_id.setter
    def page_id(self, value):
        self._page_id = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def protocol_sequence_id(self):
        return self._protocol_sequence_id

    @protocol_sequence_id.setter
    def protocol_sequence_id(self, value):
        self._protocol_sequence_id = value
    @property
    def proxy_order_url(self):
        return self._proxy_order_url

    @proxy_order_url.setter
    def proxy_order_url(self, value):
        self._proxy_order_url = value
    @property
    def report_materials_no(self):
        return self._report_materials_no

    @report_materials_no.setter
    def report_materials_no(self, value):
        self._report_materials_no = value
    @property
    def sales_img(self):
        return self._sales_img

    @sales_img.setter
    def sales_img(self, value):
        self._sales_img = value
    @property
    def sdk_voucher(self):
        return self._sdk_voucher

    @sdk_voucher.setter
    def sdk_voucher(self, value):
        self._sdk_voucher = value
    @property
    def second_channel(self):
        return self._second_channel

    @second_channel.setter
    def second_channel(self, value):
        self._second_channel = value
    @property
    def sms_code(self):
        return self._sms_code

    @sms_code.setter
    def sms_code(self, value):
        self._sms_code = value
    @property
    def target_account(self):
        return self._target_account

    @target_account.setter
    def target_account(self, value):
        self._target_account = value
    @property
    def user_agent(self):
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value):
        self._user_agent = value
    @property
    def verify_again_img(self):
        return self._verify_again_img

    @verify_again_img.setter
    def verify_again_img(self, value):
        self._verify_again_img = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_channel:
            if hasattr(self.access_channel, 'to_alipay_dict'):
                params['access_channel'] = self.access_channel.to_alipay_dict()
            else:
                params['access_channel'] = self.access_channel
        if self.advertorial_img:
            if hasattr(self.advertorial_img, 'to_alipay_dict'):
                params['advertorial_img'] = self.advertorial_img.to_alipay_dict()
            else:
                params['advertorial_img'] = self.advertorial_img
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.encrypted_mobile:
            if hasattr(self.encrypted_mobile, 'to_alipay_dict'):
                params['encrypted_mobile'] = self.encrypted_mobile.to_alipay_dict()
            else:
                params['encrypted_mobile'] = self.encrypted_mobile
        if self.first_channel:
            if hasattr(self.first_channel, 'to_alipay_dict'):
                params['first_channel'] = self.first_channel.to_alipay_dict()
            else:
                params['first_channel'] = self.first_channel
        if self.fixed_position_code:
            if hasattr(self.fixed_position_code, 'to_alipay_dict'):
                params['fixed_position_code'] = self.fixed_position_code.to_alipay_dict()
            else:
                params['fixed_position_code'] = self.fixed_position_code
        if self.inst_order_id:
            if hasattr(self.inst_order_id, 'to_alipay_dict'):
                params['inst_order_id'] = self.inst_order_id.to_alipay_dict()
            else:
                params['inst_order_id'] = self.inst_order_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.package_name:
            if hasattr(self.package_name, 'to_alipay_dict'):
                params['package_name'] = self.package_name.to_alipay_dict()
            else:
                params['package_name'] = self.package_name
        if self.package_route:
            if hasattr(self.package_route, 'to_alipay_dict'):
                params['package_route'] = self.package_route.to_alipay_dict()
            else:
                params['package_route'] = self.package_route
        if self.page_id:
            if hasattr(self.page_id, 'to_alipay_dict'):
                params['page_id'] = self.page_id.to_alipay_dict()
            else:
                params['page_id'] = self.page_id
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.protocol_sequence_id:
            if hasattr(self.protocol_sequence_id, 'to_alipay_dict'):
                params['protocol_sequence_id'] = self.protocol_sequence_id.to_alipay_dict()
            else:
                params['protocol_sequence_id'] = self.protocol_sequence_id
        if self.proxy_order_url:
            if hasattr(self.proxy_order_url, 'to_alipay_dict'):
                params['proxy_order_url'] = self.proxy_order_url.to_alipay_dict()
            else:
                params['proxy_order_url'] = self.proxy_order_url
        if self.report_materials_no:
            if hasattr(self.report_materials_no, 'to_alipay_dict'):
                params['report_materials_no'] = self.report_materials_no.to_alipay_dict()
            else:
                params['report_materials_no'] = self.report_materials_no
        if self.sales_img:
            if hasattr(self.sales_img, 'to_alipay_dict'):
                params['sales_img'] = self.sales_img.to_alipay_dict()
            else:
                params['sales_img'] = self.sales_img
        if self.sdk_voucher:
            if hasattr(self.sdk_voucher, 'to_alipay_dict'):
                params['sdk_voucher'] = self.sdk_voucher.to_alipay_dict()
            else:
                params['sdk_voucher'] = self.sdk_voucher
        if self.second_channel:
            if hasattr(self.second_channel, 'to_alipay_dict'):
                params['second_channel'] = self.second_channel.to_alipay_dict()
            else:
                params['second_channel'] = self.second_channel
        if self.sms_code:
            if hasattr(self.sms_code, 'to_alipay_dict'):
                params['sms_code'] = self.sms_code.to_alipay_dict()
            else:
                params['sms_code'] = self.sms_code
        if self.target_account:
            if hasattr(self.target_account, 'to_alipay_dict'):
                params['target_account'] = self.target_account.to_alipay_dict()
            else:
                params['target_account'] = self.target_account
        if self.user_agent:
            if hasattr(self.user_agent, 'to_alipay_dict'):
                params['user_agent'] = self.user_agent.to_alipay_dict()
            else:
                params['user_agent'] = self.user_agent
        if self.verify_again_img:
            if hasattr(self.verify_again_img, 'to_alipay_dict'):
                params['verify_again_img'] = self.verify_again_img.to_alipay_dict()
            else:
                params['verify_again_img'] = self.verify_again_img
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationDistributionFloworderCreateModel()
        if 'access_channel' in d:
            o.access_channel = d['access_channel']
        if 'advertorial_img' in d:
            o.advertorial_img = d['advertorial_img']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'encrypted_mobile' in d:
            o.encrypted_mobile = d['encrypted_mobile']
        if 'first_channel' in d:
            o.first_channel = d['first_channel']
        if 'fixed_position_code' in d:
            o.fixed_position_code = d['fixed_position_code']
        if 'inst_order_id' in d:
            o.inst_order_id = d['inst_order_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'package_name' in d:
            o.package_name = d['package_name']
        if 'package_route' in d:
            o.package_route = d['package_route']
        if 'page_id' in d:
            o.page_id = d['page_id']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'price' in d:
            o.price = d['price']
        if 'protocol_sequence_id' in d:
            o.protocol_sequence_id = d['protocol_sequence_id']
        if 'proxy_order_url' in d:
            o.proxy_order_url = d['proxy_order_url']
        if 'report_materials_no' in d:
            o.report_materials_no = d['report_materials_no']
        if 'sales_img' in d:
            o.sales_img = d['sales_img']
        if 'sdk_voucher' in d:
            o.sdk_voucher = d['sdk_voucher']
        if 'second_channel' in d:
            o.second_channel = d['second_channel']
        if 'sms_code' in d:
            o.sms_code = d['sms_code']
        if 'target_account' in d:
            o.target_account = d['target_account']
        if 'user_agent' in d:
            o.user_agent = d['user_agent']
        if 'verify_again_img' in d:
            o.verify_again_img = d['verify_again_img']
        return o


