#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenAppDeployPackageVO import OpenAppDeployPackageVO


class AlipayOpenMiniInnerdeploypackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerdeploypackageQueryResponse, self).__init__()
        self._app_deploy_package = None

    @property
    def app_deploy_package(self):
        return self._app_deploy_package

    @app_deploy_package.setter
    def app_deploy_package(self, value):
        if isinstance(value, OpenAppDeployPackageVO):
            self._app_deploy_package = value
        else:
            self._app_deploy_package = OpenAppDeployPackageVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerdeploypackageQueryResponse, self).parse_response_content(response_content)
        if 'app_deploy_package' in response:
            self.app_deploy_package = response['app_deploy_package']
