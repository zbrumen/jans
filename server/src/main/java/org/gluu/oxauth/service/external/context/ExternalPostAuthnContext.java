package org.gluu.oxauth.service.external.context;

import io.jans.model.custom.script.conf.CustomScriptConfiguration;
import org.gluu.oxauth.model.common.SessionId;
import io.jans.as.common.model.registration.Client;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * @author Yuriy Zabrovarnyy
 */
public class ExternalPostAuthnContext extends ExternalScriptContext {

    private final Client client;
    private final SessionId session;
    private CustomScriptConfiguration script;

    public ExternalPostAuthnContext(Client client, SessionId session, HttpServletRequest httpRequest, HttpServletResponse httpResponse) {
        super(httpRequest, httpResponse);
        this.client = client;
        this.session = session;
    }

    public CustomScriptConfiguration getScript() {
        return script;
    }

    public void setScript(CustomScriptConfiguration script) {
        this.script = script;
    }

    public Client getClient() {
        return client;
    }

    public SessionId getSession() {
        return session;
    }

    @Override
    public String toString() {
        return "ExternalPostAuthnContext{" +
                "client=" + client +
                ", session=" + session +
                ", script=" + script +
                "} " + super.toString();
    }
}
