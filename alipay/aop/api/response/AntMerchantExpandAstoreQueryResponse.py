#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BrandInfoModel import BrandInfoModel
from alipay.aop.api.domain.CategoryInfoModel import CategoryInfoModel
from alipay.aop.api.domain.EsStoreAuditOpenResult import EsStoreAuditOpenResult
from alipay.aop.api.domain.SettleInfoModel import SettleInfoModel


class AntMerchantExpandAstoreQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAstoreQueryResponse, self).__init__()
        self._a_store_id = None
        self._a_store_logo = None
        self._a_store_name = None
        self._biz_type = None
        self._brand_info = None
        self._category_info = None
        self._es_store_audit_result = None
        self._mobile = None
        self._oid = None
        self._out_biz_no = None
        self._settle_infos = None
        self._smid = None

    @property
    def a_store_id(self):
        return self._a_store_id

    @a_store_id.setter
    def a_store_id(self, value):
        self._a_store_id = value
    @property
    def a_store_logo(self):
        return self._a_store_logo

    @a_store_logo.setter
    def a_store_logo(self, value):
        self._a_store_logo = value
    @property
    def a_store_name(self):
        return self._a_store_name

    @a_store_name.setter
    def a_store_name(self, value):
        self._a_store_name = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def brand_info(self):
        return self._brand_info

    @brand_info.setter
    def brand_info(self, value):
        if isinstance(value, BrandInfoModel):
            self._brand_info = value
        else:
            self._brand_info = BrandInfoModel.from_alipay_dict(value)
    @property
    def category_info(self):
        return self._category_info

    @category_info.setter
    def category_info(self, value):
        if isinstance(value, CategoryInfoModel):
            self._category_info = value
        else:
            self._category_info = CategoryInfoModel.from_alipay_dict(value)
    @property
    def es_store_audit_result(self):
        return self._es_store_audit_result

    @es_store_audit_result.setter
    def es_store_audit_result(self, value):
        if isinstance(value, EsStoreAuditOpenResult):
            self._es_store_audit_result = value
        else:
            self._es_store_audit_result = EsStoreAuditOpenResult.from_alipay_dict(value)
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def settle_infos(self):
        return self._settle_infos

    @settle_infos.setter
    def settle_infos(self, value):
        if isinstance(value, SettleInfoModel):
            self._settle_infos = value
        else:
            self._settle_infos = SettleInfoModel.from_alipay_dict(value)
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAstoreQueryResponse, self).parse_response_content(response_content)
        if 'a_store_id' in response:
            self.a_store_id = response['a_store_id']
        if 'a_store_logo' in response:
            self.a_store_logo = response['a_store_logo']
        if 'a_store_name' in response:
            self.a_store_name = response['a_store_name']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'brand_info' in response:
            self.brand_info = response['brand_info']
        if 'category_info' in response:
            self.category_info = response['category_info']
        if 'es_store_audit_result' in response:
            self.es_store_audit_result = response['es_store_audit_result']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'oid' in response:
            self.oid = response['oid']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'settle_infos' in response:
            self.settle_infos = response['settle_infos']
        if 'smid' in response:
            self.smid = response['smid']
