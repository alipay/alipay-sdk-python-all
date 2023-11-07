#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayOpenAgentMobilepaySignRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._app_market = None
        self._app_name = None
        self._app_status = None
        self._app_test_account = None
        self._app_test_account_password = None
        self._app_type = None
        self._batch_no = None
        self._business_license_mobile = None
        self._business_license_no = None
        self._date_limitation = None
        self._download_link = None
        self._long_term = None
        self._mcc_code = None
        self._mobile_type = None
        self._trade_scene = None
        self._app_auth_pic = None
        self._app_demo = None
        self._app_home_screenshot = None
        self._app_item_screenshot = None
        self._app_pay_screenshot = None
        self._business_license_auth_pic = None
        self._business_license_pic = None
        self._home_screenshot = None
        self._in_app_screenshot = None
        self._pay_screenshot = None
        self._special_license_pic = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def app_market(self):
        return self._app_market

    @app_market.setter
    def app_market(self, value):
        if isinstance(value, list):
            self._app_market = list()
            for i in value:
                self._app_market.append(i)
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_status(self):
        return self._app_status

    @app_status.setter
    def app_status(self, value):
        self._app_status = value
    @property
    def app_test_account(self):
        return self._app_test_account

    @app_test_account.setter
    def app_test_account(self, value):
        self._app_test_account = value
    @property
    def app_test_account_password(self):
        return self._app_test_account_password

    @app_test_account_password.setter
    def app_test_account_password(self, value):
        self._app_test_account_password = value
    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        if isinstance(value, list):
            self._app_type = list()
            for i in value:
                self._app_type.append(i)
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def business_license_mobile(self):
        return self._business_license_mobile

    @business_license_mobile.setter
    def business_license_mobile(self, value):
        self._business_license_mobile = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def date_limitation(self):
        return self._date_limitation

    @date_limitation.setter
    def date_limitation(self, value):
        self._date_limitation = value
    @property
    def download_link(self):
        return self._download_link

    @download_link.setter
    def download_link(self, value):
        self._download_link = value
    @property
    def long_term(self):
        return self._long_term

    @long_term.setter
    def long_term(self, value):
        self._long_term = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def mobile_type(self):
        return self._mobile_type

    @mobile_type.setter
    def mobile_type(self, value):
        self._mobile_type = value
    @property
    def trade_scene(self):
        return self._trade_scene

    @trade_scene.setter
    def trade_scene(self, value):
        self._trade_scene = value

    @property
    def app_auth_pic(self):
        return self._app_auth_pic

    @app_auth_pic.setter
    def app_auth_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._app_auth_pic = value
    @property
    def app_demo(self):
        return self._app_demo

    @app_demo.setter
    def app_demo(self, value):
        if not isinstance(value, FileItem):
            return
        self._app_demo = value
    @property
    def app_home_screenshot(self):
        return self._app_home_screenshot

    @app_home_screenshot.setter
    def app_home_screenshot(self, value):
        if not isinstance(value, FileItem):
            return
        self._app_home_screenshot = value
    @property
    def app_item_screenshot(self):
        return self._app_item_screenshot

    @app_item_screenshot.setter
    def app_item_screenshot(self, value):
        if not isinstance(value, FileItem):
            return
        self._app_item_screenshot = value
    @property
    def app_pay_screenshot(self):
        return self._app_pay_screenshot

    @app_pay_screenshot.setter
    def app_pay_screenshot(self, value):
        if not isinstance(value, FileItem):
            return
        self._app_pay_screenshot = value
    @property
    def business_license_auth_pic(self):
        return self._business_license_auth_pic

    @business_license_auth_pic.setter
    def business_license_auth_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._business_license_auth_pic = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._business_license_pic = value
    @property
    def home_screenshot(self):
        return self._home_screenshot

    @home_screenshot.setter
    def home_screenshot(self, value):
        if not isinstance(value, FileItem):
            return
        self._home_screenshot = value
    @property
    def in_app_screenshot(self):
        return self._in_app_screenshot

    @in_app_screenshot.setter
    def in_app_screenshot(self, value):
        if not isinstance(value, FileItem):
            return
        self._in_app_screenshot = value
    @property
    def pay_screenshot(self):
        return self._pay_screenshot

    @pay_screenshot.setter
    def pay_screenshot(self, value):
        if not isinstance(value, FileItem):
            return
        self._pay_screenshot = value
    @property
    def special_license_pic(self):
        return self._special_license_pic

    @special_license_pic.setter
    def special_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._special_license_pic = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.open.agent.mobilepay.sign'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.app_market:
            if isinstance(self.app_market, list):
                for i in range(0, len(self.app_market)):
                    element = self.app_market[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_market[i] = element.to_alipay_dict()
                params['app_market'] = json.dumps(obj=self.app_market, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = json.dumps(obj=self.app_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_name'] = self.app_name
        if self.app_status:
            if hasattr(self.app_status, 'to_alipay_dict'):
                params['app_status'] = json.dumps(obj=self.app_status.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_status'] = self.app_status
        if self.app_test_account:
            if hasattr(self.app_test_account, 'to_alipay_dict'):
                params['app_test_account'] = json.dumps(obj=self.app_test_account.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_test_account'] = self.app_test_account
        if self.app_test_account_password:
            if hasattr(self.app_test_account_password, 'to_alipay_dict'):
                params['app_test_account_password'] = json.dumps(obj=self.app_test_account_password.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_test_account_password'] = self.app_test_account_password
        if self.app_type:
            if isinstance(self.app_type, list):
                for i in range(0, len(self.app_type)):
                    element = self.app_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_type[i] = element.to_alipay_dict()
                params['app_type'] = json.dumps(obj=self.app_type, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = json.dumps(obj=self.batch_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['batch_no'] = self.batch_no
        if self.business_license_mobile:
            if hasattr(self.business_license_mobile, 'to_alipay_dict'):
                params['business_license_mobile'] = json.dumps(obj=self.business_license_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['business_license_mobile'] = self.business_license_mobile
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = json.dumps(obj=self.business_license_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['business_license_no'] = self.business_license_no
        if self.date_limitation:
            if hasattr(self.date_limitation, 'to_alipay_dict'):
                params['date_limitation'] = json.dumps(obj=self.date_limitation.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['date_limitation'] = self.date_limitation
        if self.download_link:
            if hasattr(self.download_link, 'to_alipay_dict'):
                params['download_link'] = json.dumps(obj=self.download_link.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['download_link'] = self.download_link
        if self.long_term:
            if hasattr(self.long_term, 'to_alipay_dict'):
                params['long_term'] = json.dumps(obj=self.long_term.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['long_term'] = self.long_term
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = json.dumps(obj=self.mcc_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mcc_code'] = self.mcc_code
        if self.mobile_type:
            if hasattr(self.mobile_type, 'to_alipay_dict'):
                params['mobile_type'] = json.dumps(obj=self.mobile_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mobile_type'] = self.mobile_type
        if self.trade_scene:
            if hasattr(self.trade_scene, 'to_alipay_dict'):
                params['trade_scene'] = json.dumps(obj=self.trade_scene.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['trade_scene'] = self.trade_scene
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        if self.app_auth_pic:
            multipart_params['app_auth_pic'] = self.app_auth_pic
        if self.app_demo:
            multipart_params['app_demo'] = self.app_demo
        if self.app_home_screenshot:
            multipart_params['app_home_screenshot'] = self.app_home_screenshot
        if self.app_item_screenshot:
            multipart_params['app_item_screenshot'] = self.app_item_screenshot
        if self.app_pay_screenshot:
            multipart_params['app_pay_screenshot'] = self.app_pay_screenshot
        if self.business_license_auth_pic:
            multipart_params['business_license_auth_pic'] = self.business_license_auth_pic
        if self.business_license_pic:
            multipart_params['business_license_pic'] = self.business_license_pic
        if self.home_screenshot:
            multipart_params['home_screenshot'] = self.home_screenshot
        if self.in_app_screenshot:
            multipart_params['in_app_screenshot'] = self.in_app_screenshot
        if self.pay_screenshot:
            multipart_params['pay_screenshot'] = self.pay_screenshot
        if self.special_license_pic:
            multipart_params['special_license_pic'] = self.special_license_pic
        return multipart_params
