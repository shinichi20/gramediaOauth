DEFAULT_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'gdn_core.pipeline.gdn_auth.gdn_details',

    # Get the gdn uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'gdn_core.pipeline.gdn_auth.gdn_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    'gdn_core.pipeline.gdn_auth.auth_allowed',

    # Checks if the current gdn-account is already associated in the site.
    'gdn_core.pipeline.gdn_auth.gdn_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'gdn_core.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # 'gdn_core.pipeline.mail.mail_validation',

    # Associates the current gdn details with another user account with
    # a similar email address.
    # 'gdn_core.pipeline.gdn_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
    'gdn_core.pipeline.user.create_user',

    # Create the record that associated the gdn account with this user.
    'gdn_core.pipeline.sgdn_auth.associate_user',

    # Populate the extra_data field in the gdn record with the values
    # specified by settings (and the default ones like access_token, etc).
    'gdn_core.pipeline.gdn_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'gdn_core.pipeline.user.user_details'
)

DEFAULT_DISCONNECT_PIPELINE = (
    # Verifies that the gdn association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    'gdn_core.pipeline.disconnect.allowed_to_disconnect',

    # Collects the gdn associations to disconnect.
    'gdn_core.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'gdn_core.pipeline.disconnect.revoke_tokens',

    # Removes the gdn associations.
    'gdn_core.pipeline.disconnect.disconnect'
)