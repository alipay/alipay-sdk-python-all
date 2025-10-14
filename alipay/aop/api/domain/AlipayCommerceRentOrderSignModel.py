#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentCreditExtInfoDTO import RentCreditExtInfoDTO
from alipay.aop.api.domain.RentDoSignInfoDTO import RentDoSignInfoDTO


class AlipayCommerceRentOrderSignModel(object):

    def __init__(self):
        self._credit_ext_info = None
        self._need_face_validate_flag = None
        self._order_id = None
        self._rent_sign_info = None

    @property
    def credit_ext_info(self):
        return self._credit_ext_info

    @credit_ext_info.setter
    def credit_ext_info(self, value):
        if isinstance(value, RentCreditExtInfoDTO):
            self._credit_ext_info = value
        else:
            self._credit_ext_info = RentCreditExtInfoDTO.from_alipay_dict(value)
    @property
    def need_face_validate_flag(self):
        return self._need_face_validate_flag

    @need_face_validate_flag.setter
    def need_face_validate_flag(self, value):
        self._need_face_validate_flag = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def rent_sign_info(self):
        return self._rent_sign_info

    @rent_sign_info.setter
    def rent_sign_info(self, value):
        if isinstance(value, RentDoSignInfoDTO):
            self._rent_sign_info = value
        else:
            self._rent_sign_info = RentDoSignInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.credit_ext_info:
            if hasattr(self.credit_ext_info, 'to_alipay_dict'):
                params['credit_ext_info'] = self.credit_ext_info.to_alipay_dict()
            else:
                params['credit_ext_info'] = self.credit_ext_info
        if self.need_face_validate_flag:
            if hasattr(self.need_face_validate_flag, 'to_alipay_dict'):
                params['need_face_validate_flag'] = self.need_face_validate_flag.to_alipay_dict()
            else:
                params['need_face_validate_flag'] = self.need_face_validate_flag
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.rent_sign_info:
            if hasattr(self.rent_sign_info, 'to_alipay_dict'):
                params['rent_sign_info'] = self.rent_sign_info.to_alipay_dict()
            else:
                params['rent_sign_info'] = self.rent_sign_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderSignModel()
        if 'credit_ext_info' in d:
            o.credit_ext_info = d['credit_ext_info']
        if 'need_face_validate_flag' in d:
            o.need_face_validate_flag = d['need_face_validate_flag']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'rent_sign_info' in d:
            o.rent_sign_info = d['rent_sign_info']
        return o


