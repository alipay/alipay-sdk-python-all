#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserPersonPictureDetail import UserPersonPictureDetail


class AlipayUserAccountCertifyImageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountCertifyImageQueryResponse, self).__init__()
        self._user_person_picture_detail = None

    @property
    def user_person_picture_detail(self):
        return self._user_person_picture_detail

    @user_person_picture_detail.setter
    def user_person_picture_detail(self, value):
        if isinstance(value, list):
            self._user_person_picture_detail = list()
            for i in value:
                if isinstance(i, UserPersonPictureDetail):
                    self._user_person_picture_detail.append(i)
                else:
                    self._user_person_picture_detail.append(UserPersonPictureDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountCertifyImageQueryResponse, self).parse_response_content(response_content)
        if 'user_person_picture_detail' in response:
            self.user_person_picture_detail = response['user_person_picture_detail']
